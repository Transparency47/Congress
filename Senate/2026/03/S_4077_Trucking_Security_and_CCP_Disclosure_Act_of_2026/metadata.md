# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4077?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4077
- Title: Trucking Security and CCP Disclosure Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4077
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-04-01T20:21:23Z
- Update date including text: 2026-04-01T20:21:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4077",
    "number": "4077",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Trucking Security and CCP Disclosure Act of 2026",
    "type": "S",
    "updateDate": "2026-04-01T20:21:23Z",
    "updateDateIncludingText": "2026-04-01T20:21:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T16:09:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4077is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4077\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo ensure secure transport of Department of Defense freight, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Trucking Security and CCP Disclosure Act of 2026 .\n#### 2. Certification requirement for motor carriers transporting Department of Defense freight\nChapter 157 of title 10, United States Code, is amended by inserting after section 2631a the following new section:\n2631b. Certification regarding affiliations with Chinese military companies for surface transportation contracts (a) Certification required (1) No contract for the transportation of cargo by motor carrier for the Department of Defense (including contracts awarded by the United States Transportation Command or the Military Surface Deployment and Distribution Command) may be awarded to, or performed by, any covered carrier unless such covered carrier submits a certification described in subsection (b). (2) The requirement under paragraph (1) shall apply to prime contractors, subcontractors, and owner-operators at all tiers. (b) Contents of certification A certification under this section shall state that, to the best of the covered carrier's knowledge after reasonable inquiry\u2014 (1) the covered carrier is not owned or controlled by, and does not have significant business relationships with, any entity identified on the most recent list of Chinese military companies required under section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note); and (2) the covered carrier will require the same certification from any subcontractor or owner-operator it engages for performance of the contract. (c) Flow-Down and recordkeeping Prime contractors shall include the substance of this certification requirement in all subcontracts and lease agreements for Department of Defense freight transportation. Covered carriers shall maintain records of certifications for not less than 5 years. (d) Penalties Any covered carrier that knowingly provides a false certification under this section shall be subject to suspension or debarment from Department of Defense contracting and civil penalties under section 1001 of title 18. (e) Implementation The Secretary of Defense shall prescribe regulations to implement this section not later than 180 days after the date of the enactment of this section, including integration into existing carrier approval processes of the Military Surface Deployment and Distribution Command. (f) Definitions In this section: (1) Covered carrier The term covered carrier means any motor carrier, subcontractor, or owner-operator providing surface transportation services. (2) Significant business relationships The term significant business relationships shall have the meaning given by the Secretary of Defense in regulations. .\n#### 3. Establishment of national security registry for motor carriers handling department of defense freight\n##### (a) In general\nSubtitle IV of title 49, United States Code, is amended by inserting after chapter 139 the following:\n140 Secure Defense Freight Carrier Registry 14001. Definition of registry. 14002. Establishment of registry. 14003. Eligibility and approval. 14004. Use of registry. 14001. Definition of registry In this chapter, the term registry means the Secure Defense Freight Carrier Registry established under section 14002. 14002. Establishment of registry Not later than 1 year after the date of the enactment of this chapter, the Secretary, acting through the Administrator of the Federal Motor Carrier Safety Administration and in coordination with the Secretary of Defense, shall establish and maintain a registry, to be known as the Secure Defense Freight Carrier Registry , of motor carriers approved to transport freight for the Department of Defense. 14003. Eligibility and approval (a) Eligibility requirements To be included in the registry, a motor carrier shall\u2014 (1) hold valid operating authority from the Federal Motor Carrier Safety Administration; (2) meet all applicable Department of Defense carrier qualification standards; (3) undergo enhanced national security vetting, including\u2014 (A) screening for ownership, control, or significant business relationships with\u2014 (i) an entity identified on the list maintained by the Department of Defense under section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 10 U.S.C. 113 note; Public Law 116\u2013283 ); or (ii) any other foreign adversary entity designated by the Secretary of Defense; and (B) verification that drivers and personnel with access to Department of Defense freight meet security standards comparable to those required under Transportation Worker Identification Credential programs or other relevant Federal security programs; and (4) submit to periodic revetting not less frequently than once every 2 years. (b) Application and approval process (1) In general The Secretary shall establish a streamlined application process for inclusion on the registry. (2) Requirement The process established under paragraph (1) shall include coordination with existing Department of Defense carrier approval systems. 14004. Use of registry (a) Prohibition Subject to subsection (b), beginning 1 year after the date of the enactment of this chapter, a motor carrier may not bid on or perform a Department of Defense freight transportation contract unless the motor carrier is included in the registry. (b) Waivers The Secretary of Defense may grant waivers from the prohibition under subsection (a) for exigent circumstances. .\n##### (b) Clerical amendment\nThe analysis for subtitle IV of title 49, United States Code, is amended by inserting after the item relating to chapter 139 the following:\n140. SECURE DEFENSE FREIGHT CARRIER REGISTRY 14001 .",
      "versionDate": "2026-03-12",
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
        "actionDate": "2026-03-12",
        "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7924",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Trucking Security and CCP Disclosure Act of 2026",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-01T20:21:23Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4077is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure secure transport of Department of Defense freight, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:23Z"
    },
    {
      "title": "Trucking Security and CCP Disclosure Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Trucking Security and CCP Disclosure Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:18Z"
    }
  ]
}
```
