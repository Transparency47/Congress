# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1388?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1388
- Title: PROTECT Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1388
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1388",
    "number": "1388",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "PROTECT Act of 2025",
    "type": "S",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T19:49:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1388is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1388\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Moreno (for himself, Ms. Slotkin , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the review by the Committee on Foreign Investment in the United States of greenfield and brownfield investments by foreign countries of concern.\n#### 1. Short title\nThis Act may be cited as the Providing Rigorous Oversight Through Evaluation of Concerning Transactions Act of 2025 or the PROTECT Act of 2025 .\n#### 2. Review by Committee on Foreign Investment in the United States of greenfield and brownfield investments by foreign countries of concern\n##### (a) Inclusion in definition of covered transaction\nSection 721(a)(4) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by striking ; and and inserting a semicolon;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iii) any transaction described in subparagraph (B)(vi) proposed or pending on or after the date of the enactment of this clause. ;\n**(2)**\nin subparagraph (B), by adding at the end the following:\n(vi) Subject to subparagraphs (C) and (E), an investment by a foreign person that\u2014 (I) involves\u2014 (aa) the completed or planned purchase or lease by, or a concession to, the foreign person of private or public real estate in the United States; and (bb) the establishment of a United States business to operate a factory or other facility on that real estate; and (II) could result in control, including through formal or informal arrangements to act in concert, of that United States business by\u2014 (aa) the government of a foreign country of concern (as defined in section 10612(a) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19221(a) )); (bb) a person owned or controlled by, or acting on behalf of, such a government; (cc) an entity in which such a government has, directly or indirectly, including through formal or informal arrangements to act in concert, a 5 percent or greater interest; (dd) an entity in which such a government has, directly or indirectly, the right or power to appoint, or approve the appointment of, any members of the board of directors, board of supervisors, or an equivalent governing body (including external directors and other individuals who perform the duties usually associated with such titles) or officers (including the president, senior vice president, executive vice president, and other individuals who perform duties normally associated with such titles) of any other entity that held, directly or indirectly, including through formal or informal arrangements to act in concert, a 5 percent or greater interest in the entity in the preceding 3 years; or (ee) an entity in which any members or officers described in item (dd) of any other entity holding, directly or indirectly, including through formal or informal arrangements to act in concert, a 5 percent or greater interest in the entity are officials of such a government in the preceding 3 years. ;\n**(3)**\nin subparagraph (C)(i), in the matter preceding subclause (I), by striking subparagraph (B)(ii) and inserting clause (ii) or (vi) of subparagraph (B) ; and\n**(4)**\nin subparagraph (E), by striking clauses (ii) and (iii) and inserting clauses (ii), (iii), and (vi) .\n##### (b) Mandatory filing of declarations\nSection 721(b)(1)(C)(v)(IV)(bb) of the Defense Production Act of 1950 (50 U.S.C. 4565(b)(1)(C)(v)(IV)(bb)) is amended by adding at the end the following:\n(DD) Greenfield and brownfield investments by foreign countries of concern The parties to a covered transaction described in subsection (a)(4)(B)(vi) shall submit a declaration described in subclause (I) with respect to the transaction. .",
      "versionDate": "2025-04-09",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-22T20:42:57Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1388is.xml"
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
      "title": "PROTECT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROTECT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing Rigorous Oversight Through Evaluation of Concerning Transactions Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the review by the Committee on Foreign Investment in the United States of greenfield and brownfield investments by foreign countries of concern.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:22Z"
    }
  ]
}
```
