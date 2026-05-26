"use client";
import { Canvas, useFrame } from "@react-three/fiber";
import { Points, PointMaterial } from "@react-three/drei";
import { useRef, useState } from "react";
import * as THREE from "three";

function NebulaParticles() {
  const ref = useRef<THREE.Points>(null);
  const [positions] = useState(() => {
    const pos = new Float32Array(3000);
    for (let i = 0; i < 3000; i++) {
      pos[i] = (Math.random() - 0.5) * 10;
    }
    return pos;
  });

  useFrame((state, delta) => {
    if (ref.current) {
      ref.current.rotation.x += delta * 0.05;
      ref.current.rotation.y += delta * 0.075;
    }
  });

  return (
    <group rotation={[0, 0, Math.PI / 4]}>
      <Points ref={ref} positions={positions} stride={3} frustumCulled={false}>
        <PointMaterial
          transparent
          color="#FFD700"
          size={0.015}
          sizeAttenuation={true}
          depthWrite={false}
        />
      </Points>
    </group>
  );
}

export default function QuantNebula() {
  return (
    <div className="fixed inset-0 -z-10 bg-white">
      <Canvas camera={{ position: [0, 0, 1] }}>
        <NebulaParticles />
      </Canvas>
    </div>
  );
}
