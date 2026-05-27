import React, { useRef, useMemo } from 'react';
import { Canvas, useFrame, useThree } from '@react-three/fiber';
import { Float, MeshDistortMaterial, PerspectiveCamera } from '@react-three/drei';
import * as THREE from 'three';

const FloatingMesh = ({ position, color, speed, distort }) => {
  const mesh = useRef();
  useFrame((state) => {
    const t = state.clock.getElapsedTime();
    mesh.current.rotation.x = Math.cos(t / 4) / 2;
    mesh.current.rotation.y = Math.sin(t / 4) / 2;
    mesh.current.rotation.z = Math.sin(t / 4) / 2;
  });

  return (
    <Float speed={speed} rotationIntensity={2} floatIntensity={2}>
      <mesh ref={mesh} position={position}>
        <icosahedronGeometry args={[1, 0]} />
        <MeshDistortMaterial
          color={color}
          speed={distort}
          distort={0.4}
          radius={1}
          wireframe
        />
      </mesh>
    </Float>
  );
};

const Scene = () => {
  const { mouse } = useThree();
  const group = useRef();

  useFrame(() => {
    group.current.rotation.x = THREE.MathUtils.lerp(group.current.rotation.x, mouse.y * 0.1, 0.1);
    group.current.rotation.y = THREE.MathUtils.lerp(group.current.rotation.y, mouse.x * 0.1, 0.1);
  });

  return (
    <group ref={group}>
      <FloatingMesh position={[-3, 2, -5]} color="#F5C518" speed={1} distort={2} />
      <FloatingMesh position={[4, -2, -8]} color="#0A0F2C" speed={2} distort={1} />
      <FloatingMesh position={[-5, -4, -10]} color="#F5C518" speed={1.5} distort={3} />
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
    </group>
  );
};

const ThreeBackground = ({ opacity = 0.2 }) => {
  return (
    <div className="fixed inset-0 -z-10 pointer-events-none transition-opacity duration-1000" style={{ opacity }}>
      <Canvas>
        <PerspectiveCamera makeDefault position={[0, 0, 10]} />
        <color attach="background" args={['#F7F7F5']} />
        <Scene />
      </Canvas>
    </div>
  );
};

export default ThreeBackground;
