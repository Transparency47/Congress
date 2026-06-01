# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5961?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5961
- Title: Flood Insurance for Farmers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5961
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2026-01-23T17:06:13Z
- Update date including text: 2026-01-23T17:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5961",
    "number": "5961",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000578",
        "district": "1",
        "firstName": "Doug",
        "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
        "lastName": "LaMalfa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Flood Insurance for Farmers Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-23T17:06:13Z",
    "updateDateIncludingText": "2026-01-23T17:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5961ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5961\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. LaMalfa (for himself, Mr. Garamendi , Mr. Valadao , and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo increase the availability of flood insurance for agricultural structures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Flood Insurance for Farmers Act of 2025 .\n#### 2. Agricultural structures in special flood hazard zones\n##### (a) Requirements for State and local land use controls\nSubsection (a) of section 1315 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4022(a) ) is amended by adding at the end the following new paragraph:\n(3) Allowable local variances for certain agricultural structures (A) Requirement Notwithstanding any other provision of this Act\u2014 (i) the land use and control measures adopted pursuant to paragraph (1) may not, for purposes of such paragraph, be considered to be inadequate or inconsistent with the comprehensive criteria for land management and use under section 1361 because such measures provide that, in the case of any agricultural structure that is located in an area having special flood hazards, a variance from compliance with the requirements to elevate or floodproof such a structure and meeting the requirements of subparagraph (B) may be granted; and (ii) the Administrator may not suspend a community from participation in the national flood insurance program, or place such a community on probation under such program, because such land use and control measures provide for such a variance. This subparagraph shall not limit the ability of the Administrator to take enforcement action against a community that does not adopt adequate variance criteria or establish proper enforcement mechanisms. (B) Variance; considerations The requirements of this subparagraph with respect to a variance are as follows: (i) The variance is granted by an official from a duly constituted State or local zoning authority, or other authorized public body responsible for regulating land development or occupancy in flood-prone areas. (ii) In the case of new construction, such official has determined\u2014 (I) that neither floodproofing nor elevation of the new structure to the base flood elevation is practicable; and (II) that the structure is not located in\u2014 (aa) a designated regulatory floodway; (bb) an area riverward of a levee or other flood control structure; or (cc) an area subject to high velocity wave action or seaward of flood control structures. (iii) In the case of existing structures\u2014 (I) if such structure is substantially damaged or in need of substantial repairs or improvements, such official has determined that neither floodproofing nor elevation to the base flood elevation is practicable; and (II) if such structure is located within a designated regulatory flood\u00adway, such official has determined that the repair or improvement does not result in any increase in base flood levels during the base flood discharge. (iv) Such official has determined that the variance will not result in increased flood heights, additional threats to public safety, extraordinary public expense, create nuisances, cause fraud on or victimization of the public, or conflict with existing local laws or ordinances. (v) Not more than one claim payment exceeding $1,000 has been made for the structure under flood insurance coverage under this title within any period of 10 consecutive years at any time prior to the granting of the variance. (C) Definitions For purposes of this paragraph, the following definitions shall apply: (i) Agricultural structure The term agricultural structure has the meaning given such term in paragraph (2)(D). (ii) Floodproofing The term floodproofing means, with respect to a structure, any combination of structural and non-structural additions, changes, or adjustments to the structure, including attendant utilities and equipment, that reduce or eliminate potential flood damage to real estate or improved real property, water and sanitary facilities, structures, or their contents. .\n##### (b) Premium rates\nSection 1308 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4015 ) is amended by adding at the end the following new subsection:\n(n) Premium rates for certain agricultural structures with variances Notwithstanding any other provision of this Act, the chargeable premium rate for coverage under this title for any structure provided a variance pursuant to section 1315(a)(3) shall be the same as the rate that otherwise would apply to such structure if the structure had been dry floodproofed or a comparable actuarial rate based upon the risk associated with structures within the applicable zone. .\n#### 3. Optional coverage for umbrella policies\n##### (a) In general\nSubsection (b) of section 1306 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4013(b) ), is amended\u2014\n**(1)**\nin paragraph (4), by striking and at the end;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(6) the Administrator may provide that, in the case of any commercial property or other residential property, including multifamily rental property and agricultural property, one umbrella policy be made available to every insured upon renewal and every applicant with multiple structures on the same property, except that\u2014 (A) purchase of such coverage shall be at the option of the insured; and (B) any such coverage shall be made available only at chargeable rates that are not less than the estimated premium rates for such coverage determined in accordance with section 1307(a)(1). .\n##### (b) Report to Congress\nNot later than the expiration of the 5-year period beginning on the date of the enactment of this Act, the Administrator of the Federal Emergency Management Agency shall submit to the Congress a report evaluating the implementation of section 1306(b)(6) of the National Flood Insurance Act of 1968, as added by the amendments made by subsection (a) of this section.",
      "versionDate": "2025-11-07",
      "versionType": "Introduced in House"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-11-19T12:37:16Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5961ih.xml"
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
      "title": "Flood Insurance for Farmers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T07:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Flood Insurance for Farmers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T07:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase the availability of flood insurance for agricultural structures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T07:04:28Z"
    }
  ]
}
```
