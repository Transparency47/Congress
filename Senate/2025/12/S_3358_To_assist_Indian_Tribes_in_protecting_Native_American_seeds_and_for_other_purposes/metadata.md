# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3358?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3358
- Title: Native American Seeds Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3358
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-07T16:36:44Z
- Update date including text: 2026-01-07T16:36:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3358",
    "number": "3358",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Native American Seeds Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T16:36:44Z",
    "updateDateIncludingText": "2026-01-07T16:36:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T20:30:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
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
      "sponsorshipDate": "2025-12-04",
      "state": "ID"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "AZ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NM"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "ID"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-12-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3358is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3358\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Heinrich (for himself, Mr. Crapo , Mr. Gallego , Mr. Luj\u00e1n , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo assist Indian Tribes in protecting Native American seeds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Native American Seeds Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(2) Native American seed**\nThe term Native American seed means a seed of traditional or cultural significance to an Indian Tribe.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Protection of Native American seeds\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary shall work with Indian Tribes\u2014\n**(1)**\nto determine which seeds are Native American seeds; and\n**(2)**\nto support\u2014\n**(A)**\nefforts of Indian Tribes to protect Native American seeds;\n**(B)**\nNative American seed banks and related facilities; and\n**(C)**\ntraditional agriculture systems of Indian Tribes that provide for the nurturing and harvesting of Native American seeds.\n##### (b) Protection of information\nNotwithstanding any other provision of law, the Secretary shall not disclose or cause to be disclosed any information that is\u2014\n**(1)**\nprovided to the Secretary by an Indian Tribe for the purposes of this Act; and\n**(2)**\nidentified by the Indian Tribe as culturally sensitive, proprietary, or otherwise confidential.\n##### (c) No additional funds authorized\nNo additional funds are authorized to be appropriated to carry out this section and the activities authorized by this section are subject to the availability of appropriations made in advance for such purposes.\n#### 4. Judicial review\nNotwithstanding section 706 of title 5, United States Code, a court shall defer to the reasonable interpretation of the Secretary with respect to any ambiguous provision of this Act.",
      "versionDate": "2025-12-04",
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
        "name": "Native Americans",
        "updateDate": "2026-01-07T16:36:44Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3358is.xml"
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
      "title": "Native American Seeds Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Native American Seeds Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to assist Indian Tribes in protecting Native American seeds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:17Z"
    }
  ]
}
```
