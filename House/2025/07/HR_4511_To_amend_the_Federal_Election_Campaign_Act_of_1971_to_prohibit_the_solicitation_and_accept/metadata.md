# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4511?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4511
- Title: Uncheck the Box Act
- Congress: 119
- Bill type: HR
- Bill number: 4511
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-03-31T12:05:43Z
- Update date including text: 2026-03-31T12:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4511",
    "number": "4511",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000593",
        "district": "49",
        "firstName": "Mike",
        "fullName": "Rep. Levin, Mike [D-CA-49]",
        "lastName": "Levin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Uncheck the Box Act",
    "type": "HR",
    "updateDate": "2026-03-31T12:05:43Z",
    "updateDateIncludingText": "2026-03-31T12:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CO"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4511ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4511\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Levin (for himself, Mr. LaLota , Mr. Neguse , and Mr. Obernolte ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to prohibit the solicitation and acceptance of a recurring contribution or donation in a campaign for election for Federal office by any method which does not require the contributor or donor to give affirmative consent to making the contribution or donation on a recurring basis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Uncheck the Box Act .\n#### 2. Restrictions on solicitation and acceptance of recurring contributions or donations in campaigns for election for Federal office\n##### (a) Restrictions\nSection 324 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30126 ) is amended to read as follows:\n324. Restrictions on solicitation and acceptance of recurring contributions or donations (a) In general (1) Restrictions on solicitation A person may not solicit a recurring contribution to a political committee, a recurring contribution to fund an independent expenditure, or a recurring donation to fund an electioneering communication by any method which does not require the contributor or donor to give affirmative consent to making the contribution or donation on a recurring basis. (2) Restrictions on acceptance A political committee may not accept a contribution which was made on a recurring basis, a person funding an independent expenditure may not accept a contribution to fund the expenditure which was made on a recurring basis, and a person funding an electioneering communication may not accept a donation to fund the communication which was made on a recurring basis, unless the contributor or donor gave affirmative consent to making the contribution or donation on a recurring basis. (3) Treatment of passive actions For purposes of paragraphs (1) and (2), a contributor or donor who does not take an affirmative action to make or agree to make a contribution or donation on a recurring basis, including a contributor or donor who engages only in a passive action such as failing to uncheck a pre-checked box authorizing a recurring contribution or donation, shall not be considered to give affirmative consent to making the contribution or donation on a recurring basis. (b) Responsibilities of persons accepting contributions or donations A person accepting a contribution or donation described in subsection (a) which is made on a recurring basis shall meet the following requirements with respect to each recurrence of the contribution or donation: (1) Upon receiving the initial contribution or donation and each subsequent recurrence of the contribution or donation, the person shall provide the contributor or donor with a receipt that clearly and conspicuously discloses all of the material terms of the contribution or donation, including a statement of the date and amount of the next recurrence of the contribution or donation. (2) In addition to the information required to be provided under paragraph (1), the person shall include in each communication with the contributor or donor which relates to the contribution or donation all of the information the contributor or donor needs to cancel any subsequent recurrence of the contribution or donation. (3) Upon request of the contributor or donor, the person shall immediately cancel all subsequent recurrences of the contribution or donation which would otherwise be made after receiving the request. .\n##### (b) Effective date\nThe amendments made by this Act shall take effect on the earlier of\u2014\n**(1)**\nthe date on which the Federal Election Commission promulgates regulations to carry out section 324 of the Federal Election Campaign Act of 1971 (as amended by subsection (a)); or\n**(2)**\nthe expiration of the 180-day period which begins on the date of the enactment of this Act.",
      "versionDate": "2025-07-17",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-08-01T16:17:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-17",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr4511",
          "measure-number": "4511",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-17",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4511v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Uncheck the Box Act</strong></p><p>This bill places restrictions on recurring political contributions or donations.</p><p>Specifically, the bill prohibits any person from soliciting a recurring contribution or donation for a political committee, an independent expenditure, or an electioneering communication by any method that does not require the affirmative consent of the contributor or donor. In addition, the bill prohibits a political committee, a person funding an independent expenditure, or a person funding an electioneering communication from accepting a recurring contribution or donation unless the contributor or donor gave affirmative consent. This affirmative consent cannot be a passive action by the contributor or donor, such as failing to uncheck a prechecked box.</p><p>Further, any person who accepts a recurring contribution or donation must (1) provide a receipt for the initial contribution or donation and for each recurrence that clearly and conspicuously discloses all material terms, (2) provide all information needed to cancel the recurring contribution or donation in each communication with the contributor or donor, and (3) immediately cancel recurring contributions or donations upon request of the contributor or donor.</p>"
        },
        "title": "Uncheck the Box Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4511.xml",
    "summary": {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Uncheck the Box Act</strong></p><p>This bill places restrictions on recurring political contributions or donations.</p><p>Specifically, the bill prohibits any person from soliciting a recurring contribution or donation for a political committee, an independent expenditure, or an electioneering communication by any method that does not require the affirmative consent of the contributor or donor. In addition, the bill prohibits a political committee, a person funding an independent expenditure, or a person funding an electioneering communication from accepting a recurring contribution or donation unless the contributor or donor gave affirmative consent. This affirmative consent cannot be a passive action by the contributor or donor, such as failing to uncheck a prechecked box.</p><p>Further, any person who accepts a recurring contribution or donation must (1) provide a receipt for the initial contribution or donation and for each recurrence that clearly and conspicuously discloses all material terms, (2) provide all information needed to cancel the recurring contribution or donation in each communication with the contributor or donor, and (3) immediately cancel recurring contributions or donations upon request of the contributor or donor.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4511"
    },
    "title": "Uncheck the Box Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Uncheck the Box Act</strong></p><p>This bill places restrictions on recurring political contributions or donations.</p><p>Specifically, the bill prohibits any person from soliciting a recurring contribution or donation for a political committee, an independent expenditure, or an electioneering communication by any method that does not require the affirmative consent of the contributor or donor. In addition, the bill prohibits a political committee, a person funding an independent expenditure, or a person funding an electioneering communication from accepting a recurring contribution or donation unless the contributor or donor gave affirmative consent. This affirmative consent cannot be a passive action by the contributor or donor, such as failing to uncheck a prechecked box.</p><p>Further, any person who accepts a recurring contribution or donation must (1) provide a receipt for the initial contribution or donation and for each recurrence that clearly and conspicuously discloses all material terms, (2) provide all information needed to cancel the recurring contribution or donation in each communication with the contributor or donor, and (3) immediately cancel recurring contributions or donations upon request of the contributor or donor.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4511"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4511ih.xml"
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
      "title": "Uncheck the Box Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Uncheck the Box Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to prohibit the solicitation and acceptance of a recurring contribution or donation in a campaign for election for Federal office by any method which does not require the contributor or donor to give affirmative consent to making the contribution or donation on a recurring basis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:37Z"
    }
  ]
}
```
