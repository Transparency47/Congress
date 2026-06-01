# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4307?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4307
- Title: Protecting American Consumers from Robocalls Act
- Congress: 119
- Bill type: S
- Bill number: 4307
- Origin chamber: Senate
- Introduced date: 2026-04-15
- Update date: 2026-05-13T20:47:23Z
- Update date including text: 2026-05-13T20:47:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in Senate
- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S1786)
- Latest action: 2026-04-15: Introduced in Senate

## Actions

- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S1786)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4307",
    "number": "4307",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Protecting American Consumers from Robocalls Act",
    "type": "S",
    "updateDate": "2026-05-13T20:47:23Z",
    "updateDateIncludingText": "2026-05-13T20:47:23Z"
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
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S1786)",
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
          "date": "2026-04-15T20:05:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MN"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "HI"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "VT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-04-15",
      "state": "VT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-15",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4307is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4307\nIN THE SENATE OF THE UNITED STATES\nApril 15 (legislative day, April 14), 2026 Mr. Durbin (for himself, Ms. Smith , Ms. Hirono , Mr. Welch , Mr. Sanders , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo expand the scope of the Do Not Call rules under the Telephone Consumer Protection Act to include all telephone subscribers, to expand the private right of action for calls in violation of those rules, and to modify the definition of the term automatic telephone dialing system .\n#### 1. Short title\nThis Act may be cited as the Protecting American Consumers from Robocalls Act .\n#### 2. Expanding scope of Do Not Call rules and private right of action\n##### (a) In general\nSection 227(c) of the Communications Act of 1934 ( 47 U.S.C. 227(c) ) is amended\u2014\n**(1)**\nin paragraph (1), in the matter preceding subparagraph (A), by striking residential ;\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking residential ; and\n**(B)**\nin subparagraph (E), by striking residential ; and\n**(3)**\nin paragraph (5)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking more than one telephone call within any 12-month period by or on behalf of the same entity and inserting a telephone call by or on behalf of an entity ; and\n**(B)**\nin subparagraph (B), by striking up to .\n##### (b) Revised regulations\nNot later than 270 days after the date of enactment of this Act, the Federal Communications Commission shall revise the regulations prescribed under section 227(c) of the Communications Act of 1934 ( 47 U.S.C. 227(c) ) as necessary to implement the amendments made by subsection (a) of this section.\n#### 3. Definition of automatic telephone dialing system\nSection 227(a)(1) of the Communications Act of 1934 ( 47 U.S.C. 227(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A), by inserting or a list of telephone numbers after using a random or sequential number generator ; and\n**(2)**\nin subparagraph (B), by inserting successively without human intervention after to dial such numbers .",
      "versionDate": "2026-04-15",
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
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "8311",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting American Consumers from Robocalls Act",
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
        "name": "Commerce",
        "updateDate": "2026-05-13T20:47:23Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4307is.xml"
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
      "title": "Protecting American Consumers from Robocalls Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T04:53:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting American Consumers from Robocalls Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand the scope of the Do Not Call rules under the Telephone Consumer Protection Act to include all telephone subscribers, to expand the private right of action for calls in violation of those rules, and to modify the definition of the term \"automatic telephone dialing system\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:48:56Z"
    }
  ]
}
```
