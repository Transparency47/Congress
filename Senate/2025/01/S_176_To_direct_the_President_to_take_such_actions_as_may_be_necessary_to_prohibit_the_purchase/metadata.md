# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/176?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/176
- Title: Not One More Inch or Acre Act
- Congress: 119
- Bill type: S
- Bill number: 176
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-07-11T11:03:18Z
- Update date including text: 2025-07-11T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/176",
    "number": "176",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Not One More Inch or Acre Act",
    "type": "S",
    "updateDate": "2025-07-11T11:03:18Z",
    "updateDateIncludingText": "2025-07-11T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T16:18:50Z",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ND"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "AL"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s176is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 176\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mr. Cotton (for himself, Mr. Cramer , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo direct the President to take such actions as may be necessary to prohibit the purchase of public or private real estate located in the United States by citizens and entities of the People's Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Not One More Inch or Acre Act .\n#### 2. Prohibition on purchase of public or private real estate located in the United States by citizens and entities of the People's Republic of China\n##### (a) In general\nNotwithstanding any other provision of law, the President shall take such actions as may be necessary\u2014\n**(1)**\nto prohibit the purchase, on or after the date of the enactment of this Act, of public or private real estate located in the United States by\u2014\n**(A)**\nany citizen of the People's Republic of China;\n**(B)**\nany covered foreign entity; or\n**(C)**\nany foreign person acting for or on behalf of the Chinese Communist Party, a covered foreign entity, or a citizen of the People's Republic of China; and\n**(2)**\nif the President determines that the ownership, as of such date of enactment, by a person described in subparagraph (A), (B), or (C) of paragraph (1) of real estate located in the United States poses a national security risk to the United States, to require the sale of such real estate by not later than the date that is one year after such date of enactment.\n##### (b) Exceptions\n**(1) Exception for refugees**\nSubsection (a) does not apply with respect to a citizen of the People's Republic of China who\u2014\n**(A)**\nentered the United States as a refugee (as defined in section 101(a)(42) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(42) )); or\n**(B)**\nwas granted asylum or withholding of removal under section 208 or 241(b)(3) that Act (8 U.S.C. 1158 and 1231(b)(3)).\n**(2) Exception for property of United States nationals**\nSubsection (a)(2) does not apply with respect to the sale of real estate owned or otherwise held for personal use by a United States citizen or an alien lawfully admitted for permanent residence to the United States.\n##### (c) Definitions\nIn this section:\n**(1) Covered foreign entity**\nThe term covered foreign entity means an entity\u2014\n**(A)**\nacting on behalf of or otherwise directed by the Government of the People\u2019s Republic of China or the Chinese Communist Party;\n**(B)**\nthat\u2014\n**(i)**\nis organized under the laws of the People's Republic of China;\n**(ii)**\nhas a principal place of business in the People\u2019s Republic of China; or\n**(iii)**\nis owned or controlled by, or otherwise subject to the jurisdiction of, the Government of the People's Republic of China or the Chinese Communist Party; or\n**(C)**\nthat is a subsidiary of an entity described in subparagraph (B).\n**(2) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(3) United States**\nThe term United States means the several States, the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of the Northern Mariana Islands, American Samoa, Guam, the United States Virgin Islands, and any other territory or possession of the United States.\n**(4) United states person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States; or\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity.\n#### 3. Penalty amount under Agricultural Foreign Investment Disclosure Act of 1978\nSection 3(b) of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3502(b) ) is amended by striking exceed 25 percent of and inserting be less than 10 percent, or exceed 25 percent, of .",
      "versionDate": "2025-01-22",
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
        "updateDate": "2025-02-26T16:42:19Z"
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
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s176is.xml"
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
      "title": "Not One More Inch or Acre Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-11T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Not One More Inch or Acre Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the President to take such actions as may be necessary to prohibit the purchase of public or private real estate located in the United States by citizens and entities of the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:25Z"
    }
  ]
}
```
