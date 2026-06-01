# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3758?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3758
- Title: End Veterans Overdose Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3758
- Origin chamber: Senate
- Introduced date: 2026-02-02
- Update date: 2026-03-19T11:03:28Z
- Update date including text: 2026-03-19T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in Senate
- 2026-02-02 - IntroReferral: Introduced in Senate
- 2026-02-02 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2026-02-02: Introduced in Senate

## Actions

- 2026-02-02 - IntroReferral: Introduced in Senate
- 2026-02-02 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3758",
    "number": "3758",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "End Veterans Overdose Act of 2026",
    "type": "S",
    "updateDate": "2026-03-19T11:03:28Z",
    "updateDateIncludingText": "2026-03-19T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-02",
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
        "item": [
          {
            "date": "2026-03-18T20:00:36Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-02T22:41:22Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3758is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3758\nIN THE SENATE OF THE UNITED STATES\nFebruary 2, 2026 Mrs. Shaheen (for herself and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to make opioid overdose rescue medications available to veterans and their caregivers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End Veterans Overdose Act of 2026 .\n#### 2. Provision of opioid overdose rescue medications by Department of Veterans Affairs to veterans and their caregivers\n##### (a) In general\nThe Secretary of Veterans Affairs shall make covered medications available at pharmacies of the Department of Veterans Affairs to any covered veteran or caregiver of a covered veteran at no charge and without a prescription.\n##### (b) Provision of information\nThe Secretary shall ensure that any veteran or caregiver of a covered veteran who receives a covered medication under subsection (a) also receives drug information on the use of such medication.\n##### (c) Limitation on use of information\n**(1) In general**\nIn carrying out this section, the Secretary may only collect the personally identifiable information needed for prescribing covered medication, and any personally identifiable information collected under this section may be used solely for the purpose of delivering, evaluating, and enhancing the quality of health care.\n**(2) Exclusion**\nThe Secretary may not use any personally identifiable information collected under this section\u2014\n**(A)**\nfor the purpose of preventing a veteran from employment;\n**(B)**\nas evidence of a history of drug use; or\n**(C)**\nas evidence that an individual is an unlawful user of or addicted to any controlled substance.\n##### (d) Report\n**(1) In general**\nNot later than two years after the date on which the Secretary first makes covered medications available to covered veterans and the caregivers of covered veterans pursuant to subsection (a), and annually thereafter, the Secretary shall submit to Congress a report on this section.\n**(2) Elements**\nThe report required under paragraph (1) shall include each of the following:\n**(A)**\nThe number of covered veterans and caregivers of covered veterans who received covered medications under this section.\n**(B)**\nAn assessment of the feasibility of expanding the authority under this section to provide covered medications to immediate family members of covered veterans.\n**(C)**\nAn assessment of the feasibility of expanding the authority under this section to include non-Department health care providers through which the Secretary furnishes hospital care, medical services, and extended care services to covered veterans under section 1703 of title 38, United States Code.\n**(D)**\nAn assessment of trends in the utilization of covered medications provided under this section.\n**(E)**\nAny other recommendations of the Secretary with respect to the authority under this section.\n##### (e) Definitions\nIn this section:\n**(1) Caregiver**\nThe term caregiver means\u2014\n**(A)**\na family caregiver of a veteran participating in the program of comprehensive assistance for family caregivers under subsection (a) of section 1720G of title 38, United States Code; or\n**(B)**\na caregiver of a veteran participating in the program of general caregiver support services under subsection (b) of such section.\n**(2) Covered medication**\nThe term covered medication means any opioid overdose rescue medication, such as naloxone.\n**(3) Covered veteran**\nThe term covered veteran has the meaning given that term in section 1703(b) of title 38, United States Code.",
      "versionDate": "2026-02-02",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-02-09T19:21:37Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3758is.xml"
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
      "title": "End Veterans Overdose Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "End Veterans Overdose Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Veterans Affairs to make opioid overdose rescue medications available to veterans and their caregivers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:34Z"
    }
  ]
}
```
