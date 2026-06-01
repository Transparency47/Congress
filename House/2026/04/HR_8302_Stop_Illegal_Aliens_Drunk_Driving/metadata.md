# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8302?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8302
- Title: Stop Illegal Aliens Drunk Driving
- Congress: 119
- Bill type: HR
- Bill number: 8302
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-04-22T19:09:01Z
- Update date including text: 2026-04-22T19:09:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8302",
    "number": "8302",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Stop Illegal Aliens Drunk Driving",
    "type": "HR",
    "updateDate": "2026-04-22T19:09:01Z",
    "updateDateIncludingText": "2026-04-22T19:09:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "PA"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "TN"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8302ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8302\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mrs. Kim (for herself, Mr. Meuser , Mr. Burchett , and Mr. Joyce of Ohio ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the definition of aggravated felony in the Immigration and Nationality Act to include certain serious drunk driving offenses.\n#### 1. Short title\nThis Act may be cited as the Stop Illegal Aliens Drunk Driving .\n#### 2. Aggravated felony for driving under the influence or while intoxicated\nSection 101(a)(43) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(43) ) is amended\u2014\n**(1)**\nin subparagraph (T), by striking and at the end;\n**(2)**\nby redesignating subparagraph (U) as subparagraph (V); and\n**(3)**\nby inserting after subparagraph (T) the following:\n(U) an offense relating to driving while intoxicated, impaired, or under the influence of alcohol, a controlled substance (as defined in section 102(6) of the Controlled Substances Act ( 21 U.S.C. 802(6) )), or any other illegal narcotic or intoxicating substance\u2014 (i) which resulted in the death of, or serious bodily injury to, another person; and (ii) for which the alien was convicted, without regard to whether the conviction is classified as a misdemeanor or felony under Federal, State, tribal, or local law; and .\n#### 3. Inadmissibility for aggravated felony\nSection 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2)(F) ) is amended\u2014\n**(1)**\nby redesignating subparagraph (F) as subparagraph (J) and moving such subparagraph so that it appears immediately after subparagraph (I); and\n**(2)**\nby inserting after subparagraph (E) the following:\n(F) Aggravated felony for drunk driving or driving while intoxicated Any alien who is convicted of, admits having committed, or admits committing acts constituting the essential elements of, any law or regulation of a State, the United States, or a foreign country relating to an offense described in section 101(a)(43)(U) is inadmissible. .\n#### 4. Effective date; application\n##### (a) Effective date\nThis Act and the amendments made by this Act shall take effect on the date of the enactment of this Act.\n##### (b) Application\nThe amendments made by sections 2 and 3 shall apply\u2014\n**(1)**\nto actions taken on or after the date of the enactment of this Act, regardless of when the relevant criminal conviction occurred;\n**(2)**\nwith respect to section 276(b), only to violations of section 276(a) occurring on or after such date of enactment; and\n**(3)**\nwith respect to section 237(a)(2)(A)(iii), if the underlying aggravated felony is described in section 101(a)(43)(U) or 212(a)(2)(F), only to actions taken on or after the date of the enactment of this Act, regardless of when the relevant criminal conviction occurred.",
      "versionDate": "2026-04-15",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-01-07",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3584",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Illegal Aliens Drunk Driving",
      "type": "S"
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
        "updateDate": "2026-04-22T19:09:01Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8302ih.xml"
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
      "title": "Stop Illegal Aliens Drunk Driving",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T06:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Illegal Aliens Drunk Driving",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the definition of aggravated felony in the Immigration and Nationality Act to include certain serious drunk driving offenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T06:03:35Z"
    }
  ]
}
```
