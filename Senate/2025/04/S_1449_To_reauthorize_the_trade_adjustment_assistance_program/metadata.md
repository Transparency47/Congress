# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1449?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1449
- Title: Trade Adjustment Assistance Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1449
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-09-05T11:03:18Z
- Update date including text: 2025-09-05T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1449",
    "number": "1449",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Trade Adjustment Assistance Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2025-09-05T11:03:18Z",
    "updateDateIncludingText": "2025-09-05T11:03:18Z"
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
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
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
          "date": "2025-04-10T18:29:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "WI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "OR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "RI"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-04-10",
      "state": "VT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NY"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NY"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "AZ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1449is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1449\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Peters (for himself, Mr. Fetterman , Ms. Baldwin , Mr. Wyden , Ms. Klobuchar , Ms. Smith , Mr. Reed , Ms. Warren , Mr. Sanders , Mrs. Gillibrand , Mr. Schumer , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo reauthorize the trade adjustment assistance program.\n#### 1. Short title\nThis Act may be cited as the Trade Adjustment Assistance Reauthorization Act of 2025 .\n#### 2. Application of provisions relating to trade adjustment assistance\n##### (a) Applicability of certain provisions\nExcept as otherwise provided in this Act, the provisions of chapters 2 through 6 of title II of the Trade Act of 1974, as in effect on June 30, 2021, and as amended by this Act, shall\u2014\n**(1)**\ntake effect on the date of the enactment of this Act; and\n**(2)**\napply to petitions for certification filed under chapter 2, 3, or 6 of title II of the Trade Act of 1974 on or after such date of enactment.\n##### (b) References\nExcept as otherwise provided in this Act, whenever in this Act an amendment or repeal is expressed in terms of an amendment to, or repeal of, a provision of chapters 2 through 6 of title II of the Trade Act of 1974, the reference shall be considered to be made to a provision of any such chapter, as in effect on June 30, 2021.\n#### 3. Renewal of trade adjustment assistance program\n##### (a) Termination provisions\nSection 285 of the Trade Act of 1974 is amended by striking June 30, 2021 each place it appears and inserting December 31, 2031 .\n##### (b) Training funds\nSection 236(a)(2)(A) of the Trade Act of 1974 is amended by striking 2015 through 2021 and inserting 2026 through 2032 .\n##### (c) Reemployment trade adjustment assistance\nSection 246(b)(1) of the Trade Act of 1974 is amended by striking June 30, 2021 and inserting December 31, 2031 .\n##### (d) Authorizations of appropriations\n**(1) Trade adjustment assistance for workers**\nSection 245(a) of the Trade Act of 1974 is amended by striking June 30, 2021 and inserting December 31, 2031 .\n**(2) Trade adjustment assistance for firms**\nSection 255(a) of the Trade Act of 1974 is amended by striking 2015 through 2021 and inserting 2026 through 2032 .\n**(3) Trade adjustment assistance for farmers**\nSection 298(a) of the Trade Act of 1974 is amended by striking 2015 through 2021 and inserting 2026 through 2032 .\n#### 4. Applicability of trade adjustment assistance provisions\n##### (a) Trade adjustment assistance for workers\n**(1) Petitions filed on or after July 1, 2021, and before date of enactment**\n**(A) Certifications of workers not certified before date of enactment**\n**(i) Criteria if a determination has not been made**\nIf, as of the date of the enactment of this Act, the Secretary of Labor has not made a determination with respect to whether to certify a group of workers as eligible to apply for adjustment assistance under section 222 of the Trade Act of 1974 pursuant to a petition described in clause (iii), the Secretary shall make that determination based on the requirements of section 222 of the Trade Act of 1974, as in effect on such date of enactment.\n**(ii) Reconsideration of denials of certifications**\nIf, before the date of the enactment of this Act, the Secretary made a determination not to certify a group of workers as eligible to apply for adjustment assistance under section 222 of the Trade Act of 1974 pursuant to a petition described in clause (iii), the Secretary shall\u2014\n**(I)**\nreconsider that determination; and\n**(II)**\nif the group of workers meets the requirements of section 222 of the Trade Act of 1974, as in effect on such date of enactment, certify the group of workers as eligible to apply for adjustment assistance.\n**(iii) Petition described**\nA petition described in this clause is a petition for a certification of eligibility for a group of workers filed under section 221 of the Trade Act of 1974 on or after July 1, 2021, and before the date of the enactment of this Act.\n**(B) Eligibility for benefits**\n**(i) In general**\nExcept as provided in clause (ii), a worker certified as eligible to apply for adjustment assistance under section 222 of the Trade Act of 1974 pursuant to a petition described in subparagraph (A)(iii) shall be eligible, on and after the date that is 90 days after the date of the enactment of this Act, to receive benefits only under the provisions of chapter 2 of title II of the Trade Act of 1974, as in effect on such date of enactment.\n**(ii) Computation of maximum benefits**\nBenefits received by a worker described in clause (i) under chapter 2 of title II of the Trade Act of 1974 before the date of the enactment of this Act shall be included in any determination of the maximum benefits for which the worker is eligible under the provisions of chapter 2 of title II of the Trade Act of 1974, as in effect on the date of the enactment of this Act.\n**(2) Petitions filed before July 1, 2021**\nA worker certified as eligible to apply for adjustment assistance pursuant to a petition filed under section 221 of the Trade Act of 1974 on or before June 30, 2021, shall continue to be eligible to apply for and receive benefits under the provisions of chapter 2 of title II of such Act, as in effect on June 30, 2021.\n**(3) Qualifying separations with respect to petitions filed within 90 days of date of enactment**\nSection 223(b) of the Trade Act of 1974, as in effect on the date of the enactment of this Act, shall be applied and administered by substituting before July 1, 2021 for more than one year before the date of the petition on which such certification was granted for purposes of determining whether a worker is eligible to apply for adjustment assistance pursuant to a petition filed under section 221 of the Trade Act of 1974 on or after the date of the enactment of this Act and on or before the date that is 90 days after such date of enactment.\n##### (b) Trade adjustment assistance for firms\n**(1) Certification of firms not certified before date of enactment**\n**(A) Criteria if a determination has not been made**\nIf, as of the date of the enactment of this Act, the Secretary of Commerce has not made a determination with respect to whether to certify a firm as eligible to apply for adjustment assistance under section 251 of the Trade Act of 1974 pursuant to a petition described in subparagraph (C), the Secretary shall make that determination based on the requirements of section 251 of the Trade Act of 1974, as in effect on such date of enactment.\n**(B) Reconsideration of denial of certain petitions**\nIf, before the date of the enactment of this Act, the Secretary made a determination not to certify a firm as eligible to apply for adjustment assistance under section 251 of the Trade Act of 1974 pursuant to a petition described in subparagraph (C), the Secretary shall\u2014\n**(i)**\nreconsider that determination; and\n**(ii)**\nif the firm meets the requirements of section 251 of the Trade Act of 1974, as in effect on such date of enactment, certify the firm as eligible to apply for adjustment assistance.\n**(C) Petition described**\nA petition described in this subparagraph is a petition for a certification of eligibility filed by a firm or its representative under section 251 of the Trade Act of 1974 on or after July 1, 2021, and before the date of the enactment of this Act.\n**(2) Certification of firms that did not submit petitions between July 1, 2021, and date of enactment**\n**(A) In general**\nThe Secretary of Commerce shall certify a firm described in subparagraph (B) as eligible to apply for adjustment assistance under section 251 of the Trade Act of 1974, as in effect on the date of the enactment of this Act, if the firm or its representative files a petition for a certification of eligibility under section 251 of the Trade Act of 1974 not later than 90 days after such date of enactment.\n**(B) Firm described**\nA firm described in this subparagraph is a firm that the Secretary determines would have been certified as eligible to apply for adjustment assistance if\u2014\n**(i)**\nthe firm or its representative had filed a petition for a certification of eligibility under section 251 of the Trade Act of 1974 on a date during the period beginning on July 1, 2021, and ending on the day before the date of the enactment of this Act; and\n**(ii)**\nthe provisions of chapter 3 of title II of the Trade Act of 1974, as in effect on such date of enactment, had been in effect on that date during the period described in clause (i).",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-14T15:09:24Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1449is.xml"
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
      "title": "Trade Adjustment Assistance Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-05T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Trade Adjustment Assistance Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the trade adjustment assistance program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:37Z"
    }
  ]
}
```
