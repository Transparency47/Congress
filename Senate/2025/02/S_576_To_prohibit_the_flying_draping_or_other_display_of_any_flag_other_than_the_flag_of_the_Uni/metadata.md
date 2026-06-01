# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/576?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/576
- Title: One Flag for All Act
- Congress: 119
- Bill type: S
- Bill number: 576
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/576",
    "number": "576",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "One Flag for All Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T18:02:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "MS"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WY"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "MS"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s576is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 576\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Marshall (for himself, Mrs. Hyde-Smith , Ms. Lummis , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit the flying, draping, or other display of any flag other than the flag of the United States at covered public buildings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Flag for All Act .\n#### 2. Prohibition on flags other than the flag of the United States\n##### (a) Definitions\nIn this section:\n**(1) Covered public building**\n**(A) In general**\nExcept as provided in subparagraph (B), the term covered public building has the meaning given the term public building in section 3301(a) of title 40, United States Code.\n**(B) Inclusions**\nThe term covered public building includes\u2014\n**(i)**\na building in use by the Senate or House of Representatives or otherwise under the jurisdiction of the Architect of the Capitol;\n**(ii)**\na military installation; and\n**(iii)**\nany embassy or consulate of the United States.\n**(2) Flag of the United States**\nThe term flag of the United States has the meaning given the term in section 700(b) of title 18, United States Code.\n**(3) Military installation**\nThe term military installation has the meaning given the term in section 2801(c) of title 10, United States Code.\n##### (b) Prohibitions\nNotwithstanding any other provision of law, and except as provided in subsection (c), no flag that is not the flag of the United States may be flown, draped, or otherwise displayed\u2014\n**(1)**\non the exterior of a covered public building; or\n**(2)**\nin an area of a covered public building that is fully accessible to the public, including an entryway or hallway.\n##### (c) Exceptions\nThe prohibitions under subsection (b) shall not apply to\u2014\n**(1)**\na National League of Families POW/MIA flag (as designated by section 902(a) of title 36, United States Code);\n**(2)**\na Hostage and Wrongful Detainee flag (as designated by section 904(a) of title 36, United States Code);\n**(3)**\nany flag that represents the nation of a visiting diplomat or a representative of the government of that nation visiting the covered public building at which the flag is displayed;\n**(4)**\nin the case of a Member of Congress, the State flag of the State represented by the Member that is located outside or within the office of the Member;\n**(5)**\nany flag that represents a unit or branch of the Armed Forces or any flag that supports the Armed Forces;\n**(6)**\nany flag of historical significance to the United States, including the Betsy Ross flag, the Gadsden flag, and the Bennington flag;\n**(7)**\nany flag that represents public safety;\n**(8)**\nany flag commemorating a special national observance, including any 9/11 memorial, Remembrance Day, Veterans Day, or Memorial Day flag;\n**(9)**\nin the case of a religious liturgy or ceremony at a military installation or facility, any flag that represents a religious organization or church that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of that Code;\n**(10)**\nin the case of a Federal agency, any flag that represents the Federal agency;\n**(11)**\nany flag that represents an Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); or\n**(12)**\nany flag that represents the State, territory, county, city, or local jurisdiction in which the covered public building is located.",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-13",
        "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management."
      },
      "number": "1313",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Flag for All Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-07-08T13:05:33Z"
          },
          {
            "name": "Military facilities and property",
            "updateDate": "2025-07-08T13:05:33Z"
          },
          {
            "name": "National symbols",
            "updateDate": "2025-07-08T13:05:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-12T22:42:52Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s576is.xml"
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
      "title": "One Flag for All Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "One Flag for All Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the flying, draping, or other display of any flag other than the flag of the United States at covered public buildings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:13Z"
    }
  ]
}
```
