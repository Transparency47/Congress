# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3584?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3584
- Title: Stop Illegal Aliens Drunk Driving
- Congress: 119
- Bill type: S
- Bill number: 3584
- Origin chamber: Senate
- Introduced date: 2026-01-07
- Update date: 2026-04-22T19:08:52Z
- Update date including text: 2026-04-22T19:08:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in Senate
- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-07: Introduced in Senate

## Actions

- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3584",
    "number": "3584",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Stop Illegal Aliens Drunk Driving",
    "type": "S",
    "updateDate": "2026-04-22T19:08:52Z",
    "updateDateIncludingText": "2026-04-22T19:08:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-07",
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
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T18:04:25Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "AZ"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "NC"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "NC"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "WY"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TN"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "LA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "MO"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "OK"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3584is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3584\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2026 Mr. Cornyn (for himself, Mr. Cruz , Mr. Gallego , Mr. Budd , Mr. Tillis , Ms. Lummis , Mr. Hagerty , Mr. Kennedy , Mr. Schmitt , Mr. Lankford , and Mr. Mullin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the definition of aggravated felony in the Immigration and Nationality Act to include certain serious drunk driving offenses.\n#### 1. Short title\nThis Act may be cited as the Stop Illegal Aliens Drunk Driving .\n#### 2. Aggravated felony for driving under the influence or while intoxicated\nSection 101(a)(43) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(43) ) is amended\u2014\n**(1)**\nin subparagraph (T), by striking and at the end;\n**(2)**\nby redesignating subparagraph (U) as subparagraph (V); and\n**(3)**\nby inserting after subparagraph (T) the following:\n(U) an offense relating to driving while intoxicated, impaired, or under the influence of alcohol, a controlled substance (as defined in section 102(6) of the Controlled Substances Act ( 21 U.S.C. 802(6) )), or any other illegal narcotic or intoxicating substance\u2014 (i) which resulted in the death of, or serious bodily injury to, another person; and (ii) for which the alien was convicted, without regard to whether the conviction is classified as a misdemeanor or felony under Federal, State, tribal, or local law; and .\n#### 3. Inadmissibility for aggravated felony\nSection 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2)(F) ) is amended\u2014\n**(1)**\nby redesignating subparagraph (F) as subparagraph (J) and moving such subparagraph so that it appears immediately after subparagraph (I); and\n**(2)**\nby inserting after subparagraph (E) the following:\n(F) Aggravated felony for drunk driving or driving while intoxicated Any alien who is convicted of, admits having committed, or admits committing acts constituting the essential elements of, any law or regulation of a State, the United States, or a foreign country relating to an offense described in section 101(a)(43)(U) is inadmissible. .\n#### 4. Effective date; application\n##### (a) Effective date\nThis Act and the amendments made by this Act shall take effect on the date of the enactment of this Act.\n##### (b) Application\nThe amendments made by sections 2 and 3 shall apply\u2014\n**(1)**\nto actions taken on or after the date of the enactment of this Act, regardless of when the relevant criminal conviction occurred;\n**(2)**\nwith respect to section 276(b), only to violations of section 276(a) occurring on or after such date of enactment; and\n**(3)**\nwith respect to section 237(a)(2)(A)(iii), if the underlying aggravated felony is described in section 101(a)(43)(U) or 212(a)(2)(F), only to actions taken on or after the date of the enactment of this Act, regardless of when the relevant criminal conviction occurred.",
      "versionDate": "2026-01-07",
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
        "actionDate": "2026-04-15",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "8302",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Illegal Aliens Drunk Driving",
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
        "name": "Immigration",
        "updateDate": "2026-02-04T16:21:40Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3584is.xml"
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
      "title": "Stop Illegal Aliens Drunk Driving",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T11:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Illegal Aliens Drunk Driving",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the definition of aggravated felony in the Immigration and Nationality Act to include certain serious drunk driving offenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:55Z"
    }
  ]
}
```
