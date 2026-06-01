# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5899?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5899
- Title: Caring for Mothers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5899
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2025-12-11T09:07:19Z
- Update date including text: 2025-12-11T09:07:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5899",
    "number": "5899",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Caring for Mothers Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-11T09:07:19Z",
    "updateDateIncludingText": "2025-12-11T09:07:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5899ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5899\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Ms. Van Duyne introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXVII of the Public Health Service Act to increase health insurance access for individuals placing their newborns for adoption.\n#### 1. Short title\nThis Act may be cited as the Caring for Mothers Act of 2025 .\n#### 2. Increasing health insurance access for individuals placing their newborns for adoption\n##### (a) In general\nSubpart II of part A of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u201311 et seq. ) is amended by adding at the end the following new section:\n2730. Availability of coverage for individuals placing their newborns for adoption (a) In general In the case of an individual enrolled in a group health plan or group or individual health insurance coverage who intends to adopt (or has already adopted) a child of a qualifying individual and who submits to such plan or coverage (as applicable) a request described in subsection (b) with respect to such qualifying individual, such plan or coverage shall enroll such qualifying individual under such plan or coverage and provide benefits under such plan or coverage in accordance with subsection (c). (b) Request For purposes of subsection (a), a request described in this subsection is a request submitted to a group health plan or group or individual health insurance coverage by an individual who is enrolled in such plan or coverage who intends to adopt (or has already adopted) a biological child of a qualifying individual that\u2014 (1) requests that such qualifying individual receive benefits under such plan or coverage in accordance with subsection (c); (2) contains an attestation that such individual intends to adopt (or already has adopted) such child; (3) in the case such child has not been so adopted at the time of the submission of such request, contains an attestation from such qualifying individual that such qualifying individual intends to have such individual adopt such child; and (4) is signed by such individual and such qualifying individual. (c) Coverage (1) Scope Notwithstanding any other provisions of law, benefits provided under a group health plan or group or individual health insurance coverage to a qualifying individual enrolled pursuant to a request described in subsection (b) shall consist only of\u2014 (A) pregnancy-related and postpartum care; and (B) mental health and substance use disorder services. (2) Coverage period Coverage provided under a group health plan or group or individual health insurance coverage to a qualifying individual pursuant to a request described in subsection (b) shall begin on the first day of the first month beginning after the date such plan or coverage receives such request and shall end on the earliest of the following: (A) The date the individual who submitted such request notifies such plan or coverage of such individual\u2019s intent to terminate such coverage. (B) The date on which coverage of such individual under such plan or group or individual health insurance coverage is terminated. (C) The date such qualifying individual notifies such plan or coverage of such qualifying individual\u2019s intent to terminate such coverage. (D) The date that is 1 year after the date of the birth of the child that is the subject of the adoption described in subsection (a). (d) Clarification on scope of requirement The requirement on a group health plan or group or individual health insurance coverage under subsection (a) to provide benefits to a qualifying individual pursuant to a request described in subsection (b) shall apply only with respect to benefits described in subsection (c)(1) furnished with respect to the pregnancy that is the subject of the adoption described in subsection (b). (e) Qualifying individual defined In this section, the term qualifying individual means an individual who\u2014 (1) is pregnant or who has given birth in the last 6 months; and (2) is a citizen or national of the United States or an alien lawfully present in the United States. (f) Rule of construction Nothing in this section may be construed to\u2014 (1) require a qualifying individual who enrolls in a group health plan or group or individual health insurance coverage pursuant to this section, or an individual who requests enrollment of such qualifying individual in such plan or coverage, to effectuate any adoption; or (2) allow for the imposition of any penalty on such a qualifying individual or individual requesting such enrollment if such an adoption is not effectuated. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply with respect to plan years beginning on or after January 1, 2026.",
      "versionDate": "2025-10-31",
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
        "name": "Health",
        "updateDate": "2025-11-25T16:45:40Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5899ih.xml"
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
      "title": "Caring for Mothers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Caring for Mothers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXVII of the Public Health Service Act to increase health insurance access for individuals placing their newborns for adoption.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T07:48:19Z"
    }
  ]
}
```
