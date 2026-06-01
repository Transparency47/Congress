# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4295?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4295
- Title: Stop Support for UNRWA Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4295
- Origin chamber: Senate
- Introduced date: 2026-04-15
- Update date: 2026-05-12T11:03:32Z
- Update date including text: 2026-05-12T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in Senate
- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-04-15: Introduced in Senate

## Actions

- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4295",
    "number": "4295",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Stop Support for UNRWA Act of 2026",
    "type": "S",
    "updateDate": "2026-05-12T11:03:32Z",
    "updateDateIncludingText": "2026-05-12T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:20:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "WY"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "TN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NE"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "SC"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "ND"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NC"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "UT"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4295is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4295\nIN THE SENATE OF THE UNITED STATES\nApril 15 (legislative day, April 14), 2026 Mr. Scott of Florida (for himself, Mr. Barrasso , Mr. Hagerty , Mr. Ricketts , Mr. Scott of South Carolina , Mr. Hoeven , Mrs. Britt , Mr. Budd , and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo prohibit aid that would benefit Hamas, to place restrictions on funding for United Nations entities that are led by countries that support terrorism, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Stop Support for United Nations Relief and Works Agency Act of 2026 or the Stop Support for UNRWA Act of 2026 .\n#### 2. Prohibition against United States contributions to UNRWA\nThe United States may not make any voluntary or involuntary contributions to the United Nations Relief and Works Agency for Palestine Refugees in the Near East (referred to in this Act as UNRWA ), to any successor or related entity to UNRWA, or to the regular budget of the United Nations for the support of UNRWA or such successor or related entity.\n#### 3. Restrictions on United Nations delegations and organizations\n##### (a) Restrictions on United States delegations\nFederal funds may not be used to pay any expenses for any United States delegation to any specialized agency, body, or commission of the United Nations if such agency, body, or commission is chaired or presided over by a country, the government of which the Secretary of State has determined, for purposes of section 1754(c) of the Export Reform Control Act of 2018 ( 50 U.S.C. 4813(c) ), has repeatedly provided support for acts of international terrorism.\n##### (b) Restrictions on contributions\nFederal funds may not be used by the Secretary of State as a contribution to any organization, agency, commission, or program within the United Nations system if such organization, agency, commission, or program is chaired or presided over by a country the government of which the Secretary of State has determined, for purposes of section 620A(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371(a) ), section 40 of the Arms Export Control Act ( 22 U.S.C. 2780 ), section 1754(c) of the Export Reform Control Act of 2018 ( 50 U.S.C. 4813(c) ), or any other provision of law, is a government that has repeatedly provided support for acts of international terrorism.\n##### (c) Revocation of immunities\nNotwithstanding any other provision of law, no official, employee, or representative of UNRWA shall be entitled to any of the privileges, exemptions, or immunities otherwise provided under the International Organizations Immunities Act ( 22 U.S.C. 288 et seq. ) or under any other provision of law or Executive order.",
      "versionDate": "2026-04-15",
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
        "name": "International Affairs",
        "updateDate": "2026-04-23T18:51:24Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4295is.xml"
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
      "title": "Stop Support for UNRWA Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Support for UNRWA Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T05:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Support for United Nations Relief and Works Agency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T05:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit aid that would benefit Hamas, to place restrictions on funding for United Nations entities that are led by countries that support terrorism, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T05:48:27Z"
    }
  ]
}
```
