import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Stars } from '@react-three/drei';

const ParticleField = () => {
  const ref = useRef();
  useFrame((state) => {
    ref.current.rotation.y = state.clock.getElapsedTime() * 0.05;
    ref.current.rotation.x = state.clock.getElapsedTime() * 0.02;
  });
  return (
    <group ref={ref}>
      <Stars radius={100} depth={50} count={5000} factor={4} saturation={0} fade speed={1} />
    </group>
  );
};

const ThreeBackground = ({ opacity = 0.1 }) => {
  return (
    <div className="fixed inset-0 -z-10 pointer-events-none" style={{ opacity }}>
      <Canvas camera={{ position: [0, 0, 5] }}>
        <color attach="background" args={['#0A0F2C']} />
        <ParticleField />
      </Canvas>
    </div>
  );
};

export default ThreeBackground;
