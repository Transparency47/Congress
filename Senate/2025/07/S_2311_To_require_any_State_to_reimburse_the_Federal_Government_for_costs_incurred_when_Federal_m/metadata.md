# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2311?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2311
- Title: State Accountability for Federal Deployment Costs Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2311
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2025-12-05T22:56:57Z
- Update date including text: 2025-12-05T22:56:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2311",
    "number": "2311",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "State Accountability for Federal Deployment Costs Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:56:57Z",
    "updateDateIncludingText": "2025-12-05T22:56:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T22:16:12Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2311is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2311\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mrs. Blackburn (for herself and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require any State to reimburse the Federal Government for costs incurred when Federal military forces are deployed in response to civil disturbances or security threats caused by the State\u2019s refusal to cooperate with lawful Federal immigration enforcement.\n#### 1. Short title\nThis Act may be cited as the State Accountability for Federal Deployment Costs Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nImmigration enforcement is a constitutionally and statutorily delegated power of the Federal Government.\n**(2)**\nCertain States and units of local government have refused to assist with, or have actively obstructed, lawful Federal immigration enforcement operations, including by refusing to comply with immigration detainer requests and obstructing Federal immigration enforcement operations (commonly referred to as raids ).\n**(3)**\nSuch noncompliance and obstruction can result in civil unrest, security breakdowns, and law enforcement emergencies that require the deployment of Federal military forces, including the National Guard under section 12406 of title 10, United States Code, or active-duty military personnel.\n**(4)**\nSuch deployments impose substantial costs on the Department of Defense and United States taxpayers, which should be reimburse by the States and units of local government whose noncompliance with or obstruction of Federal immigration enforcement actions created the need for such deployments.\n#### 3. Reimbursement requirement\n##### (a) In general\nThe Secretary of Defense shall submit a reimbursement invoice to the Governor of the affected State whenever Federal military personnel (including members of the National Guard and units of the Selected Reserve) are deployed, under Federal authority, to any jurisdiction as a direct result of\u2014\n**(1)**\ncivil disturbances stemming from lawful Federal immigration enforcement operations; and\n**(2)**\nthe failure of a State or unit of local government to provide reasonable cooperation or coordination with such operations.\n##### (b) Covered costs\nCost that are reimbursable under subsection (a) shall include\u2014\n**(1)**\ntemporary duty travel (TDY) and per diem for Federal military personnel deployed in accordance with subsection (a);\n**(2)**\nhousing, lodging, and meals for such personnel; and\n**(3)**\ntransportation of such personnel and their equipment.\n##### (c) Determination of noncooperation\nThe Secretary of Homeland Security, in consultation with the Attorney General, shall issue a public determination as to whether the actions or omissions of a State or unit of local government materially hindered or failed to support the Federal immigration enforcement operations that led to the deployment of Federal military personnel.\n##### (d) Payment and offset\n**(1) Payment due date**\nEach State shall remit full payment of an invoice received pursuant to subsection (a) not later than 180 days after receiving such invoice from the Department of Defense.\n**(2) Offset**\nIf a State fails to remit a payment in accordance with paragraph (1), the President, in consultation with the Secretary of Defense, the Secretary of Homeland Security, the Attorney General, and the heads of other Federal departments or agencies, as appropriate, may rescind 1 or more discretionary grants awarded to the State by the Federal Government to offset such nonpayment.",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-07-17",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Oversight and Government Reform, and Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4483",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "State Accountability for Federal Deployment Costs Act of 2025",
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
        "updateDate": "2025-08-07T18:49:42Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2311is.xml"
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
      "title": "State Accountability for Federal Deployment Costs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T06:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "State Accountability for Federal Deployment Costs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require any State to reimburse the Federal Government for costs incurred when Federal military forces are deployed in response to civil disturbances or security threats caused by the State's refusal to cooperate with lawful Federal immigration enforcement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:24Z"
    }
  ]
}
```
