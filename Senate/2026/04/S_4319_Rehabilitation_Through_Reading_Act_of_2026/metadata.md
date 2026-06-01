# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4319?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4319
- Title: Rehabilitation Through Reading Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4319
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-05-13T17:13:23Z
- Update date including text: 2026-05-13T17:13:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-16: Introduced in Senate

## Actions

- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4319",
    "number": "4319",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Rehabilitation Through Reading Act of 2026",
    "type": "S",
    "updateDate": "2026-05-13T17:13:23Z",
    "updateDateIncludingText": "2026-05-13T17:13:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T16:57:29Z",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "HI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NJ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "VT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4319is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4319\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Schiff (for himself, Ms. Hirono , Mr. Booker , Mr. Welch , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require an independent review process for the prohibition of books at Bureau of Prisons facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rehabilitation Through Reading Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Director**\nThe term Director means the Director of the Bureau of Prisons.\n**(2) Professional librarian**\nThe term professional librarian means a librarian who has a master's degree from a program accredited by the American Library Association.\n#### 3. Banned books in prisons\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, the Director shall establish a Publication Review Committee for the purpose of approving or disapproving the availability of books at Bureau of Prisons facilities.\n##### (b) Members\nThe Publication Review Committee shall consist of not fewer than 5 members, including the Ombudsman established under section 2 of the Federal Prison Oversight Act ( Public Law 118\u201371 ), 1 individual who is a professional librarian employed by the Bureau of Prisons, 1 individual in the custody of the Bureau of Prisons, and 1 individual with knowledge or expertise in First Amendment law.\n##### (c) Procedures\n**(1) Prohibiting a book**\nFollowing the date of the establishment of the Publication Review Committee, the Director may only prohibit a book at Bureau of Prisons facilities if\u2014\n**(A)**\nthe Director submits a request in writing to the Publication Review Committee to approve such prohibition, including a detailed explanation of the reason for prohibiting the book; and\n**(B)**\nthe Publication Review Committee approves such request.\n**(2) Appeal of a prohibited book**\nAn individual in the custody of the Bureau of Prisons may submit to the Publication Review Committee an appeal to reverse the prohibition of a book in Bureau of Prisons facilities.\n**(3) Determinations**\n**(A) In general**\nNot later than 90 days after the date on which a request or appeal is submitted to the Publication Review Committee under paragraph (1) or (2), as applicable, the Publication Review Committee shall issue a final determination in writing approving or disapproving the availability of the book at Bureau of Prisons facilities in accordance with subparagraph (B).\n**(B) Reason for prohibiting a book**\n**(i) In general**\nA book may not be prohibited in order to eliminate a disfavored viewpoint or disfavored content.\n**(ii) Considerations**\nIn determining whether the prohibition of a book is based on a disfavored viewpoint or disfavored content, the Publication Review Committee shall determine whether the prohibition is substantially motivated by the viewpoint of the book, including if the book is deemed unpopular or repugnant, or otherwise violates the rights of incarcerated individuals to access information.\n**(C) Discretion**\nExcept as provided in subparagraph (B), a determination issued by the Publication Review Committee shall be at the discretion of the Publication Review Committee and shall not require approval from the Director.\n**(4) Maintaining access to a book**\nIf an appeal is filed under paragraph (2) prior to the removal of the book from any library of any Bureau of Prisons facility, the book shall not be removed until the Publication Review Committee has made a final determination regarding the appeal.\n#### 4. Annual reporting requirement\nNot later than 30 days after the end of each fiscal year following the date of enactment of this Act, the Director shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives an annual report detailing any books that were prohibited during the preceding fiscal year, including a summary of each appeal filed pursuant to section 3(c)(2) and the status and final outcome, as applicable, of each appeal.",
      "versionDate": "2026-04-16",
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
        "actionDate": "2026-04-16",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "8325",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Rehabilitation Through Reading Act of 2026",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-13T17:13:23Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4319is.xml"
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
      "title": "Rehabilitation Through Reading Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T04:53:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rehabilitation Through Reading Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require an independent review process for the prohibition of books at Bureau of Prisons facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:48:59Z"
    }
  ]
}
```
