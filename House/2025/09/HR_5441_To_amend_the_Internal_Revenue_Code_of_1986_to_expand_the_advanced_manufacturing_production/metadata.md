# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5441?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5441
- Title: Fusion Advanced Manufacturing Parity Act
- Congress: 119
- Bill type: HR
- Bill number: 5441
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2026-03-25T08:06:00Z
- Update date including text: 2026-03-25T08:06:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-17: Introduced in House

## Actions

- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5441",
    "number": "5441",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Fusion Advanced Manufacturing Parity Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:00Z",
    "updateDateIncludingText": "2026-03-25T08:06:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-09-17T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "NY"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "WA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "VA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "VA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "KS"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "CA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "WA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "CA"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "VA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NY"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5441ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5441\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Mrs. Miller of West Virginia (for herself, Ms. Tenney , Ms. DelBene , and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the advanced manufacturing production credit to include fusion energy components.\n#### 1. Short title\nThis Act may be cited as the Fusion Advanced Manufacturing Parity Act .\n#### 2. Inclusion of fusion energy components in advanced manufacturing production credit\n##### (a) In general\nSection 45X of the Internal Revenue Code of 1986, as amended by section 70514 of Public Law 119\u201321 , is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (L)(ii), by striking and at the end,\n**(ii)**\nby redesignating subparagraph (M) as subparagraph (N), and\n**(iii)**\nby inserting after subparagraph (L) the following new subparagraph:\n(M) in the case of a fusion energy component, an amount equal to 25 percent of the sales price of such component, and ,\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking and (D) and inserting , (D), and (E) ,\n**(ii)**\nby redesignating subparagraphs (D) and (E) as subparagraphs (E) and (F), respectively, and\n**(iii)**\nby inserting after subparagraph (C) the following new subparagraph:\n(D) Phase out for fusion energy components (i) In general In the case of any fusion energy component sold after December 31, 2031, the amount determined under this subsection with respect to such component shall be equal to the product of\u2014 (I) the amount determined under paragraph (1) with respect to such component, as determined without regard to this paragraph, multiplied by (II) the phase out percentage under clause (ii). (ii) Phase out percentage The phase out percentage under this clause is equal to\u2014 (I) in the case of a fusion energy component sold during calendar year 2032, 75 percent, (II) in the case of a fusion energy component sold during calendar year 2033, 50 percent, (III) in the case of a fusion energy component sold during calendar year 2034, 25 percent, and (IV) in the case of a fusion energy component sold after December 31, 2034, 0 percent. , and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A)\u2014\n**(i)**\nby redesignating clauses (iv) and (v) as clauses (v) and (vi), respectively, and\n**(ii)**\nby inserting after clause (iii) the following new clause:\n(iv) any fusion energy component, ,\n**(B)**\nby redesignating paragraph (6) as paragraph (7),\n**(C)**\nby inserting after paragraph (5) the following new paragraph:\n(6) Fusion energy component (A) In general The term fusion energy component means any of the following components which are intended for the operation or use of a fusion energy machine: (i) A high-temperature superconducting magnet. (ii) A fusion chamber or plasma vacuum vessel. (iii) A blanket system. (iv) High-temperature superconductor tape or wire. (v) A high-energy laser. (vi) A fusion heating system. (vii) A high-voltage capacitor. (viii) Films used in high-voltage capacitors. (ix) Plasma compression systems. (x) High-power switches. (xi) Packaging used in high-power switches. (xii) High-voltage conductors and insulators. (xiii) Composite materials used in fusion chambers or vacuum vessels. (xiv) Fused quartz parts and ceramics used in fusion chambers or vacuum vessels. (xv) Plasma formation devices. (xvi) Fuel processing and storage components. (xvii) Cooling system components. (xviii) Fusion targets. (xix) Dielectric fluids and systems. (xx) Controls equipment. (B) Fusion energy machine The term fusion energy machine means a fusion machine (as defined in section 11 of the Atomic Energy Act of 1954 ( 42 U.S.C. 2014 )) which is used for the production of electricity or process heat, as well as any associated system (such as for fuel and exhaust processing). (C) High-temperature superconducting magnet The term high-temperature superconducting magnet means the entire system of electromagnetic coils consisting of high-temperature superconducting tape and structural metals that produce the magnetic fields, which confine, shape, and stabilize the plasma in a fusion energy machine, including toroidal field magnets, poloidal field magnets, and central solenoid magnets. (D) Fusion chamber or plasma vacuum vessel The term fusion chamber or plasma vacuum vessel means the enclosing structure that\u2014 (i) holds fusion targets or creates and maintains a vacuum in the area which contains the fusion plasma, and (ii) absorbs the plasma heat exhaust and structurally supports other integrated components, such as the plasma facing material, in-vessel diagnostics, and plasma heating systems in the fusion energy machine. (E) Blanket system The term blanket system means the containers, pipes, pumps, chemistry control, tritium and fuel extractors, heat exchangers, and liquid metal, salt bath, or other components that are designed to remove the fusion heat, shield components from neutrons, generate tritium, and transfer heat to a power generation system. (F) High-temperature superconductor tape or wire The term high-temperature superconductor tape or wire means the multi-layered tape or foil that carries electrical current with no resistance at high temperatures and magnetic fields. (G) High-energy laser The term high-energy laser means the sources of light and associated optic systems that transfer beams of light to either directly or indirectly implode a fusion fuel capsule to create a fusion reaction. (H) Fusion heating system The term fusion heating system means an auxiliary system used to increase the temperature of fusion fuel to create fusion reactions. (I) High-voltage capacitor The term high-voltage capacitor means an electrical component designed to store and release electrical energy in circuits operating at high voltage levels above 1,000 volts, as well as circuit components (such as printed circuit boards) used to enable the capacitor system or related power system to function. (J) Films used in high-voltage capacitors The term films used in high-voltage capacitors means metalized and non-metalized films used due to their dielectric properties, high breakdown voltage, and thermal stability in windings for high-voltage capacitors. (K) Plasma compression system The term plasma compression system means mechanical or electrical components, such as electromagnetic coils or gas-driven pistons, used to compress plasma targets. (L) High-power switches The term high-power switches means switching devices which\u2014 (i) use semiconductors, electrodes and a gas chamber, or other approaches, and (ii) are used to control and manage the flow of power in circuits by enabling or interrupting the flow of high voltage or high current greater than 1 kilovolt. (M) Packaging used in high-power switches The term packaging used in high-power switches means covers, terminals, or connections, heat transfer components, or packaging surrounding a semiconductor die. (N) High-voltage conductors and insulators The term high-voltage conductors and insulators means power transmission components used to connect high-voltage capacitors to fusion energy machines, including cables and busbars capable of operating greater than 1 kilovolt or 1 kiloampere. (O) Composite materials used in vacuum vessels The term composite materials used in vacuum vessels means fiber reinforced materials, such as glass-epoxy systems, used to create vacuum chambers for fusion energy machines. (P) Fused quartz and ceramic parts used in vacuum vessels The term fused quartz parts and ceramics used in vacuum vessels means components made of high-purity quartz material or other dielectric ceramics and machined into components used as plasma-facing components on fusion energy machine vacuum vessels. (Q) Plasma formation device The term plasma formation device means components used to form fusion plasmas through methods such as coaxial helicity injection or local helicity injection. (R) Fuel processing and storage components The term fuel processing and storage components means components used for the manufacture, purification, processing, transport, or storage of fusion fuels, including deuterium, tritium, and helium-3. (S) Cooling system components The term cooling system components includes chillers, fluid coolers, distribution systems, and similar components that cool mechanical or electrical components (such as high-temperature superconducting magnets) during normal operations. (T) Fusion targets The term fusion targets means components that\u2014 (i) contain the fusion fuel in the fusion chamber, and (ii) receive energy from lasers or electrical circuits to cause such fusion fuel to undergo a fusion reaction. (U) Dielectric fluids and systems The term dielectric fluids and systems means\u2014 (i) electrically insulated fluids, such as transformer oil or deionized water used for electrical insulation, and (ii) any associated equipment needed to move and maintain the physical properties of such fluids, such as pumps, filtration systems, and cooling systems. (V) Controls equipment The term controls equipment means any hardware or software used to electronically control any subsystem of a fusion energy machine. , and\n**(D)**\nin paragraph (7) (as redesignated by subparagraph (B) of this paragraph)\u2014\n**(i)**\nin subparagraph (D)(i), by inserting beryllium hydroxide, or beryllium fluoride, after copper-beryllium master alloy, ,\n**(ii)**\nin subparagraph (P)(i), by striking or lithium hydroxide and inserting , lithium hydroxide, lithium chloride, lithium fluoride, lithium-6, lithium-7, or lithium tetrafluoroberyllate ,\n**(iii)**\nby striking subparagraphs (X) and (Y) and inserting the following:\n(X) Tungsten Tungsten which is\u2014 (i) converted to tungsten master alloy, (ii) converted to ammonium paratungstate, ferrotungsten, tungsten trioxide, or tungsten carbide, or (iii) purified to a minimum purity of 85 percent tungsten by mass. (Y) Vanadium Vanadium which is\u2014 (i) converted to vanadium master alloy, (ii) converted to ferrovanadium or vanadium pentoxide, or (iii) purified to a minimum purity of 85 percent vanadium by mass. ,\n**(iv)**\nin subparagraph (AA)\u2014\n**(I)**\nby redesignating clauses (xxiii) through (xxv) as clauses (xxvi) through (xxviii), respectively,\n**(II)**\nby redesignating clauses (vii) through (xxii) as clauses (ix) through (xxiv), respectively,\n**(III)**\nby redesignating clauses (iii) through (vi) as clauses (iv) through (vii), respectively,\n**(IV)**\nby inserting after clause (ii) the following new clause:\n(iii) Deuterium. ,\n**(V)**\nby inserting after clause (vii) (as redesignated by subclause (III) of this clause) the following new clause:\n(viii) Helium\u20133. , and\n**(VI)**\nby inserting after clause (xxiv) (as redesignated by subclause (II) of this clause) the following new clause:\n(xxv) Tritium. ,\n**(v)**\nby redesignating subparagraphs (I) through (AA) as subparagraphs (K) through (CC), respectively,\n**(vi)**\nby redesignating subparagraphs (E) through (H) as subparagraphs (F) through (I), respectively,\n**(vii)**\nby inserting after subparagraph (D) the following new subparagraph:\n(E) Boron Boron which is converted to boron carbide or ferroboron. , and\n**(viii)**\nby inserting after subparagraph (I) (as redesignated by clause (vi) of this paragraph) the following new subparagraph:\n(J) Copper chromium zirconium Alloys or assemblies comprised of not less than 80 percent copper. .\n##### (b) Conforming amendment\nSection 30D(e)(1)(A) of the Internal Revenue Code of 1986 is amended by striking section 45X(c)(6) and inserting section 45X(c)(7) .\n##### (c) Effective date\nThe amendments made by this section shall apply to components produced and sold after December 31, 2025.",
      "versionDate": "2025-09-17",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-30",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3088",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fusion Advanced Manufacturing Parity Act",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-11-21T15:55:00Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5441ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Fusion Advanced Manufacturing Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T04:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fusion Advanced Manufacturing Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand the advanced manufacturing production credit to include fusion energy components.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:14Z"
    }
  ]
}
```
