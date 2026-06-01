# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1661?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1661
- Title: Disaster Relief for Farmworkers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1661
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-06-05T13:28:57Z
- Update date including text: 2025-06-05T13:28:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1661",
    "number": "1661",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Disaster Relief for Farmworkers Act of 2025",
    "type": "S",
    "updateDate": "2025-06-05T13:28:57Z",
    "updateDateIncludingText": "2025-06-05T13:28:57Z"
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
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
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
          "date": "2025-05-07T21:11:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1661is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1661\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Bennet (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 with respect to emergency assistance for farmworkers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Relief for Farmworkers Act of 2025 .\n#### 2. Emergency assistance for farmworkers\nSection 2281 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 42 U.S.C. 5177a ) is amended to read as follows:\n2281. Emergency assistance for farmworkers (a) Definitions In this section: (1) Covered disaster The term covered disaster means\u2014 (A) an adverse weather event, such as a drought, wildfire, earthquake, hurricane, flood, derecho, excessive heat, tornado, winter storm, freeze, hail, polar vortex, smoke exposure, or excessive moisture; (B) an unexpected health crisis, such as a pandemic; and (C) such other event or condition that has caused farmworkers to lose income, be unable to work, or stay home or return home in anticipation of work shortages. (2) Eligible farmworker organization The term eligible farmworker organization means an organization that is\u2014 (A) a farmworker membership-based organization; or (B) an organization\u2014 (i) described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of that Code; and (ii) that has experience in providing support or relief services to farmworkers, including migrant or seasonal farmworkers. (3) Migrant or seasonal farmworker The term migrant or seasonal farmworker means an individual\u2014 (A) who has, during any consecutive 12-month period within the preceding 24-month period, performed farm work for wages; and (B) who has received not less than \u00bd of such individual\u2019s total income from, or been employed at least \u00bd of such individual's total work time in, farm work. (4) Secretary The term Secretary means the Secretary of Agriculture. (b) Emergency relief For fiscal year 2024 and each succeeding fiscal year, during any period for which the Secretary determines there is a covered disaster, the Secretary, acting through the Under Secretary for Rural Development, shall make grants to eligible farmworker organizations to provide emergency relief to farmworkers affected by that covered disaster. (c) Use of funds An eligible farmworker organization may use funds received pursuant to a grant awarded under subsection (b)\u2014 (1) to provide emergency relief (including through direct distribution of funding) to farmworkers to address loss and damage due to the covered disaster; (2) to build capacity to provide emergency relief described in paragraph (1); (3) to build resiliency in farmworker communities to address future losses and damages due to covered disasters; (4) to provide infrastructure support, including shelter; and (5) to provide emergency services (including such types of assistance as the Secretary determines to be appropriate) to farmworkers in response to the covered disaster. (d) Availability of funds Any funds provided to an eligible farmworker organization under this section shall remain available until expended. (e) Promotional plan The Secretary shall\u2014 (1) before making grants under subsection (b), develop a promotional plan; and (2) carry out that promotional plan throughout the distribution of those grants. (f) Consultation In carrying out this section, the Secretary shall consult with eligible farmworker organizations. .",
      "versionDate": "2025-05-07",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-05T13:28:57Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1661is.xml"
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
      "title": "Disaster Relief for Farmworkers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disaster Relief for Farmworkers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food, Agriculture, Conservation, and Trade Act of 1990 with respect to emergency assistance for farmworkers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:30Z"
    }
  ]
}
```
