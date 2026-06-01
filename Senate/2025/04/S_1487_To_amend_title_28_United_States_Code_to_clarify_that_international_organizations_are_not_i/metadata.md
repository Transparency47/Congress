# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1487?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1487
- Title: LIABLE Act
- Congress: 119
- Bill type: S
- Bill number: 1487
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1487",
    "number": "1487",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "LIABLE Act",
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
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T21:46:19Z",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ND"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NC"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NE"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MT"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TN"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "WY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1487is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1487\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Cruz (for himself, Mr. Cramer , Mr. Budd , Mr. Ricketts , Mr. Daines , Mr. Hagerty , Mr. Barrasso , Mr. Scott of Florida , and Mr. Schmitt ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to clarify that international organizations are not immune from the jurisdiction of the courts of the United States in certain cases related to terrorism.\n#### 1. Short title\nThis Act may be cited as the Limiting Immunity for Assisting Backers of Lethal Extremism Act or the LIABLE Act .\n#### 2. Terrorism exception to the jurisdictional immunity of an international organization\n##### (a) In general\nPart IV of title 28, United States Code, is amended by inserting after chapter 97 the following:\n97A Jurisdictional immunities of international organizations Sec. 1621. Terrorism exception to the jurisdictional immunity of an international organization. 1621. Terrorism exception to the jurisdictional immunity of an international organization (a) Definitions In this section: (1) Aircraft sabotage; armed forces; extrajudicial killing; hostage taking; material support or resources; national of the United States The terms aircraft sabotage , armed forces , extrajudicial killing , hostage taking , material support or resources , and national of the United States have the meanings given the terms in section 1605A. (2) International organization The term international organization \u2014 (A) has the meaning given the term in section 1 of the International Organizations Immunities Act ( 22 U.S.C. 288 ); and (B) includes agencies or affiliated entities of organizations described in that section. (b) Exception (1) No immunity An international organization shall not be immune from the jurisdiction of courts of the United States or of the States in any case not otherwise covered by the International Organizations Immunity Act ( 22 U.S.C. 288 et seq. ) in which money damages are sought against an international organization for personal injury or death that was caused by an act of torture, extrajudicial killing, aircraft sabotage, hostage taking, or the provision of material support or resources for such an act if such act or provision of material support or resources is engaged in by an official, employee, or agent of such international organization while acting within the scope of his or her office, employment, or agency. (2) Claim heard The court shall hear a claim under this section if\u2014 (A) the international organization conspired with, materially supported, or otherwise aided and abetted an organization designated as a foreign terrorist organization under section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ); and (B) (i) the claimant or the victim was, at the time the act described in paragraph (1) occurred\u2014 (I) a national of the United States; (II) a member of the armed forces; and (III) otherwise an employee of the Government of the United States, or of an individual performing a contract awarded by the United States Government, acting within the scope of the employment of the employee; or (ii) the international organization is based in or has a substantial presence in the United States. (c) Limitations An action may be brought or maintained under this section if the action is commenced not later than 20 years after the date on which the cause of action arose. .\n##### (b) Technical and conforming amendment\nThe table of chapters for part IV of title 28, United States Code, is amended by inserting after the item relating to chapter 97 the following:\n97A. Jurisdictional immunities of international organizations 1621 .",
      "versionDate": "2025-04-10",
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
        "name": "Law",
        "updateDate": "2025-05-20T14:05:52Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1487is.xml"
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
      "title": "LIABLE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LIABLE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Limiting Immunity for Assisting Backers of Lethal Extremism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 28, United States Code, to clarify that international organizations are not immune from the jurisdiction of the courts of the United States in certain cases related to terrorism.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:27Z"
    }
  ]
}
```
