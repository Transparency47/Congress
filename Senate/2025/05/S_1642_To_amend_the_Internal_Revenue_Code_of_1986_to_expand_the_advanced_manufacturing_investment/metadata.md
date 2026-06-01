# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1642?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1642
- Title: SEMI Investment Act
- Congress: 119
- Bill type: S
- Bill number: 1642
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-12-17T15:03:17Z
- Update date including text: 2025-12-17T15:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1642",
    "number": "1642",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "SEMI Investment Act",
    "type": "S",
    "updateDate": "2025-12-17T15:03:17Z",
    "updateDateIncludingText": "2025-12-17T15:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-05-07T19:19:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CO"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1642is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1642\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mrs. Blackburn (for herself, Mr. Bennet , Mr. Tillis , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the advanced manufacturing investment credit to include materials integral to semiconductor manufacturing.\n#### 1. Short title\nThis Act may be cited as the Strengthening Essential Manufacturing and Industrial Investment Act or the SEMI Investment Act .\n#### 2. Expansion of advanced manufacturing investment credit\n##### (a) In general\nParagraph (3) of section 48D(b) of the Internal Revenue Code of 1986 is amended to read as follows:\n(3) Advanced manufacturing facility (A) In general For purposes of this section, the term advanced manufacturing facility means a facility for which the primary purpose is the manufacturing of\u2014 (i) semiconductors, (ii) semiconductor manufacturing equipment, or (iii) semiconductor materials. (B) Semiconductor materials (i) In general For purposes of this paragraph, the term semiconductor materials means\u2014 (I) any direct production material, or (II) any indirect production material, which is used in semiconductor manufacturing (as defined in section 231.116 of title 15, Code of Federal Regulations). (ii) Direct production material For purposes of this subparagraph, the term direct production material means a material which is\u2014 (I) primarily used for, and integral to, the production of a semiconductor, (II) physically incorporated into a finished semiconductor, and (III) any of the following: (aa) Substrate Any substrate of silicon, silicon carbide, gallium nitride, gallium arsenide, indium phosphide, or other semiconductor-grade substrate material. (bb) Thin film or layering material Any deposited metal, dielectric, barrier material, or dopant that forms the physical structure of a semiconductor. (cc) Packaging substrate material Any ceramic, organic, or metallic material that forms the physical base for semiconductor packaging. (dd) Bonding, interconnect, or adhesive material Any wire bond, solder bump, lead frame, die attach adhesive, underfill, or other material which\u2014 (AA) forms electrical connections within a semiconductor, or (BB) provides structural integrity within a semiconductor. (iii) Indirect production material (I) In general For purposes of this subparagraph, the term indirect production material means a material which is\u2014 (aa) a specialized material that is primarily used for, and integral to, the production, testing, inspection, or packaging of a semiconductor, (bb) not physically incorporated into a finished semiconductor, and (cc) any of the following: (AA) Process chemicals An etchant, deposition precursor, doping gas, or other chemical used in wafer fabrication. (BB) Photolithography material A photoresist, photoresist ancillary material, developer, mask, or pellicle used in semiconductor patterning. (CC) Cleaning, planarization, and preparation material A solvent, surfactant, slurry, Chemical Mechanical Planarization (CMP) pad, conditioning disk, or cleaning agent used to prepare and maintain semiconductor manufacturing surfaces. (DD) Testing and inspection material A probe card, test socket, or optical inspection material. (EE) Packaging process material A mold compound, encapsulant, or bonding wire used in assembly processes. (FF) Fluid-, gas-, or wafer-handling material A polymer, elastomer, ceramic material and resultant tubings, fittings, vessels, filters, seals, or other such chemical-handling or wafer-handling material. (GG) Wafer processing chamber materials Any process chamber materials used in production that play an active role in energy transmission, heat dissipation, plasma resistance, or chemical resistance. (HH) Other material Any other material identified by the Secretary pursuant to subclause (II). (II) Other indirect production materials For purposes of item (cc)(HH) of subclause (I), the Secretary (in consultation with the Secretary of Commerce) shall identify additional materials which are described in items (aa) and (bb) of such subclause. (III) Exclusion The term indirect production material shall not include any material which\u2014 (aa) has a generic use, and (bb) is predominately used in an application other than semiconductor manufacturing. (iv) List of semiconductor materials (I) In general Not later than 180 days after the date of enactment of the Strengthening Essential Manufacturing and Industrial Investment Act , and annually thereafter, the Secretary, in consultation with the Secretary of Commerce, shall publish a list that sets forth the specifications, characteristics, and applications of materials that qualify as direct production materials and indirect production materials for purposes of clauses (ii) and (iii). (II) Petition for interim determination In the case of any material which has not been included on the most recent list under subclause (I), a taxpayer may file a petition (at such time, and in such form and manner, as the Secretary may prescribe) with the Secretary for a determination of whether such material qualifies as a direct production material or indirect production material for purposes of clauses (ii) and (iii). .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after the date of enactment of this Act.",
      "versionDate": "2025-05-07",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-11-17",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "6055",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SEMI Investment Act",
      "type": "HR"
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
        "updateDate": "2025-06-09T14:56:52Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1642is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SEMI Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Essential Manufacturing and Industrial Investment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to expand the advanced manufacturing investment credit to include materials integral to semiconductor manufacturing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:16Z"
    }
  ]
}
```
