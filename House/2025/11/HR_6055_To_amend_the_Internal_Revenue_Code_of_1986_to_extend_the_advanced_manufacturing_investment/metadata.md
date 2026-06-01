# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6055?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6055
- Title: SEMI Investment Act
- Congress: 119
- Bill type: HR
- Bill number: 6055
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2026-05-20T08:08:28Z
- Update date including text: 2026-05-20T08:08:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-17: Introduced in House

## Actions

- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6055",
    "number": "6055",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "SEMI Investment Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:28Z",
    "updateDateIncludingText": "2026-05-20T08:08:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-17",
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
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-17",
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
          "date": "2025-11-17T17:01:20Z",
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
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "PA"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "ME"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "DE"
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
      "sponsorshipDate": "2025-12-02",
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
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6055ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6055\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Mr. Fitzpatrick (for himself, Mr. Boyle of Pennsylvania , Mr. Golden of Maine , and Ms. McBride ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the advanced manufacturing investment credit and include materials integral to semiconductor manufacturing.\n#### 1. Short title\nThis Act may be cited as the Strengthening Essential Manufacturing and Industrial Investment Act or the SEMI Investment Act .\n#### 2. Expansion and extension of advanced manufacturing investment credit\n##### (a) In general\nParagraph (3) of section 48D(b) of the Internal Revenue Code of 1986 is amended to read as follows:\n(3) Advanced manufacturing facility (A) In general For purposes of this section, the term advanced manufacturing facility means a facility for which the primary purpose is the manufacturing of\u2014 (i) semiconductors, (ii) semiconductor manufacturing equipment, or (iii) semiconductor materials. (B) Semiconductor materials (i) In general For purposes of this paragraph, the term semiconductor materials means\u2014 (I) any direct production material, or (II) any indirect production material, which is used in semiconductor manufacturing (as defined in section 231.116 of title 15, Code of Federal Regulations). (ii) Direct production material For purposes of this subparagraph, the term direct production material means a material which is\u2014 (I) primarily used for, and integral to, the production of a semiconductor, (II) physically incorporated into a finished semiconductor, and (III) any of the following: (aa) Substrate Any substrate of silicon, silicon carbide, gallium nitride, gallium arsenide, indium phosphide, or other semiconductor-grade substrate material. (bb) Thin film or layering material Any deposited metal, dielectric, barrier material, or dopant that forms the physical structure of a semiconductor. (cc) Packaging substrate material Any ceramic, organic, or metallic material that forms the physical base for semiconductor packaging. (dd) Bonding, interconnect, or adhesive material Any wire bond, solder bump, lead frame, die attach adhesive, underfill, or other material which\u2014 (AA) forms electrical connections within a semiconductor, or (BB) provides structural integrity within a semiconductor. (iii) Indirect production material (I) In general For purposes of this subparagraph, the term indirect production material means a material which is\u2014 (aa) a specialized material that is primarily used for, and integral to, the production, testing, inspection, or packaging of a semiconductor, (bb) not physically incorporated into a finished semiconductor, and (cc) any of the following: (AA) Process chemicals An etchant, deposition precursor, doping gas, or other chemical used in wafer fabrication. (BB) Photolithography material A photoresist, photoresist ancillary material, developer, mask, or pellicle used in semiconductor patterning. (CC) Cleaning, planarization, and preparation material A solvent, surfactant, slurry, Chemical Mechanical Planarization (CMP) pad, conditioning disk, or cleaning agent used to prepare and maintain semiconductor manufacturing surfaces. (DD) Testing and inspection material A probe card, test socket, or optical inspection material. (EE) Packaging process material A mold compound, encapsulant, or bonding wire used in assembly processes. (FF) Fluid-, gas-, or wafer-handling material A polymer, elastomer, ceramic material and resultant tubings, fittings, vessels, filters, seals, or other such chemical-handling or wafer-handling material. (GG) Wafer processing chamber materials Any process chamber materials used in production that play an active role in energy transmission, heat dissipation, plasma resistance, or chemical resistance. (HH) Other material Any other material identified by the Secretary pursuant to subclause (II). (II) Other indirect production materials For purposes of item (cc)(HH) of subclause (I), the Secretary (in consultation with the Secretary of Commerce) shall identify additional materials which are described in items (aa) and (bb) of such subclause. (III) Exclusion The term indirect production material shall not include any material which\u2014 (aa) has a generic use, and (bb) is predominately used in an application other than semiconductor manufacturing. (iv) List of semiconductor materials (I) In general Not later than 180 days after the date of enactment of the Strengthening Essential Manufacturing and Industrial Investment Act , and annually thereafter, the Secretary, in consultation with the Secretary of Commerce, shall publish a list that sets forth the specifications, characteristics, and applications of materials that qualify as direct production materials and indirect production materials for purposes of clauses (ii) and (iii). (II) Petition for interim determination In the case of any material which has not been included on the most recent list under subclause (I), a taxpayer may file a petition (at such time, and in such form and manner, as the Secretary may prescribe) with the Secretary for a determination of whether such material qualifies as a direct production material or indirect production material for purposes of clauses (ii) and (iii). .\n##### (b) Credit period extension\nSection 48D(e) of such Code is amended by striking December 31, 2026 and inserting December 31, 2031 .\n##### (c) Effective date\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall apply to property placed in service after the date of the enactment of this Act.\n**(2) Credit period extension**\nThe amendment made by subsection (b) shall apply to property, the construction of which begins after December 31, 2026.",
      "versionDate": "2025-11-17",
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
        "actionDate": "2025-05-07",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1642",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SEMI Investment Act",
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
        "updateDate": "2025-11-25T19:26:38Z"
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
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6055ih.xml"
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
      "title": "SEMI Investment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-22T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEMI Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-22T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Essential Manufacturing and Industrial Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-22T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to extend the advanced manufacturing investment credit and include materials integral to semiconductor manufacturing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-22T04:33:22Z"
    }
  ]
}
```
