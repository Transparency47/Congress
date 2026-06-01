# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1884?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1884
- Title: Veterans Fellowship Act
- Congress: 119
- Bill type: HR
- Bill number: 1884
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-12-19T09:08:07Z
- Update date including text: 2025-12-19T09:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1884",
    "number": "1884",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Veterans Fellowship Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:08:07Z",
    "updateDateIncludingText": "2025-12-19T09:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NV"
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
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1884ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1884\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Moolenaar (for himself and Ms. Scholten ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Assistant Secretary of Labor for Veterans\u2019 Employment and Training to carry out a pilot program on short-term fellowship programs for veterans.\n#### 1. Short title\nThis Act may be cited as the Veterans Fellowship Act .\n#### 2. Pilot program on short-term fellowship programs\n##### (a) Authority\nThe Assistant Secretary of Labor for Veterans' Employment and Training shall carry out a pilot program under which a State may use a grant or contract under section 4102A(b)(5) of title 38, United States Code, to carry out a short-term fellowship program.\n##### (b) Locations; agreements\nThe Assistant Secretary shall select at least three, but not more than five, States to carry out a short-term fellowship program pursuant to subsection (a). Each such State shall enter into an agreement with a non-profit organization to carry out such program.\n##### (c) Short-Term fellowship program\nEach short-term fellowship program carried out by a State pursuant to subsection (a) shall\u2014\n**(1)**\nconsist of veterans participating as fellows with an employer for a period not exceeding 20 weeks;\n**(2)**\nprovide to such veterans a monthly stipend during such period; and\n**(3)**\nprovide to such veterans an opportunity to be employed on a long-term basis with the employer following such period.\n##### (d) Comptroller General report\nNot later than four years after the date on which the pilot program commences under this section, the Comptroller General of the United States shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report on the pilot program.\n##### (e) Authorization of appropriations\nIn addition to funds made available under section 4102A(b)(5) of title 38, United States Code, there is authorized to be appropriated to the Assistant Secretary to carry out the pilot program under this section $10,000,000 for each of fiscal years 2025 through 2029.",
      "versionDate": "2025-03-05",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T15:08:14Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1884ih.xml"
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
      "title": "Veterans Fellowship Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Fellowship Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Assistant Secretary of Labor for Veterans' Employment and Training to carry out a pilot program on short-term fellowship programs for veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:59Z"
    }
  ]
}
```
