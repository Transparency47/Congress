# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/98?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/98
- Title: A resolution condemning Beijing's destruction of Hong Kong's democracy and rule of law.
- Congress: 119
- Bill type: SRES
- Bill number: 98
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2025-05-08T19:34:25Z
- Update date including text: 2025-05-08T19:34:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1400-1401)
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 57.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S1400-1401)
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 57.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/98",
    "number": "98",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "A resolution condemning Beijing's destruction of Hong Kong's democracy and rule of law.",
    "type": "SRES",
    "updateDate": "2025-05-08T19:34:25Z",
    "updateDateIncludingText": "2025-05-08T19:34:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 57.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment and with a preamble. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S1400-1401)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-26",
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
        "item": [
          {
            "date": "2025-04-28T20:40:16Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-27T17:55:25Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-26T16:39:27Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "DE"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "LA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "GA"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "KY"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "VA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "ID"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MD"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "TN"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "IN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres98is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 98\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Risch (for himself and Mrs. Shaheen ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCondemning Beijing\u2019s destruction of Hong Kong\u2019s democracy and rule of law.\nThat the Senate\u2014\n**(1)**\ncondemns the Government of the People\u2019s Republic of China\u2019s Hong Kong national security law , the Hong Kong government\u2019s Safeguarding National Security Ordinance , and related abuses of internationally recognized human rights;\n**(2)**\nurges all governments that value democracy or autonomy to hold the Chinese Communist Party and the Hong Kong authorities accountable for their destruction of Hong Kong\u2019s autonomy, rule of law, and freedoms;\n**(3)**\nsupports the people of Hong Kong as they fight to exercise fundamental rights and freedoms, as enumerated by\u2014\n**(A)**\nthe Joint Declaration of the Government of the United Kingdom of Great Britain and Northern Ireland and the Government of the People's Republic of China on the Question of Hong Kong, done at Beijing December 19, 1984;\n**(B)**\nthe International Covenant on Civil and Political Rights, done at New York December 19, 1966; and\n**(C)**\nthe Universal Declaration of Human Rights, done at Paris December 10, 1948;\n**(4)**\ncondemns the Government of the People\u2019s Republic of China\u2019s practice of bringing false and politically motivated charges against Hong Kongers and the expansion of Hong Kong\u2019s national security regime that destroys the rule of law and undermines citizens\u2019 rights in Hong Kong;\n**(5)**\ncalls upon the Hong Kong government to immediately drop all sedition, national security law, and Article 23-related charges and free all defendants immediately, including Jimmy Lai;\n**(6)**\nexpresses extreme concern about the Government of the People's Republic of China' state-directed theft of Apple Daily, and holds that Hong Kong no longer has credibility as an international business center due to the erosion of the regulatory, legal, and judicial environments that have promoted its economic growth for decades;\n**(7)**\nencourages the United States Government and other governments to take steps at multilateral institutions to ensure that voting procedures recognize that there is no longer a meaningful distinction between Hong Kong and mainland China; and\n**(8)**\nurges the United States Government to use all available and appropriate tools, including those authorized by the Hong Kong Human Rights and Democracy Act, in response to the Government of the People\u2019s Republic of China\u2019s actions in Hong Kong.",
      "versionDate": "2025-02-26",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres98rs.xml",
      "text": "III\nCalendar No. 57\n119th CONGRESS\n1st Session\nS. RES. 98\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Risch (for himself, Mrs. Shaheen , Mr. Coons , Mr. Cassidy , Mr. Warnock , Mr. McConnell , Mr. Kaine , Mr. Crapo , Ms. Hassan , and Mr. Van Hollen ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nApril 28, 2025 Reported by Mr. Risch , without amendment\nRESOLUTION\nCondemning Beijing\u2019s destruction of Hong Kong\u2019s democracy and rule of law.\nThat the Senate\u2014\n**(1)**\ncondemns the Government of the People\u2019s Republic of China\u2019s Hong Kong national security law , the Hong Kong government\u2019s Safeguarding National Security Ordinance , and related abuses of internationally recognized human rights;\n**(2)**\nurges all governments that value democracy or autonomy to hold the Chinese Communist Party and the Hong Kong authorities accountable for their destruction of Hong Kong\u2019s autonomy, rule of law, and freedoms;\n**(3)**\nsupports the people of Hong Kong as they fight to exercise fundamental rights and freedoms, as enumerated by\u2014\n**(A)**\nthe Joint Declaration of the Government of the United Kingdom of Great Britain and Northern Ireland and the Government of the People's Republic of China on the Question of Hong Kong, done at Beijing December 19, 1984;\n**(B)**\nthe International Covenant on Civil and Political Rights, done at New York December 19, 1966; and\n**(C)**\nthe Universal Declaration of Human Rights, done at Paris December 10, 1948;\n**(4)**\ncondemns the Government of the People\u2019s Republic of China\u2019s practice of bringing false and politically motivated charges against Hong Kongers and the expansion of Hong Kong\u2019s national security regime that destroys the rule of law and undermines citizens\u2019 rights in Hong Kong;\n**(5)**\ncalls upon the Hong Kong government to immediately drop all sedition, national security law, and Article 23-related charges and free all defendants immediately, including Jimmy Lai;\n**(6)**\nexpresses extreme concern about the Government of the People's Republic of China' state-directed theft of Apple Daily, and holds that Hong Kong no longer has credibility as an international business center due to the erosion of the regulatory, legal, and judicial environments that have promoted its economic growth for decades;\n**(7)**\nencourages the United States Government and other governments to take steps at multilateral institutions to ensure that voting procedures recognize that there is no longer a meaningful distinction between Hong Kong and mainland China; and\n**(8)**\nurges the United States Government to use all available and appropriate tools, including those authorized by the Hong Kong Human Rights and Democracy Act, in response to the Government of the People\u2019s Republic of China\u2019s actions in Hong Kong.",
      "versionDate": "2025-04-28",
      "versionType": "RS"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Asia",
            "updateDate": "2025-04-16T17:51:05Z"
          },
          {
            "name": "China",
            "updateDate": "2025-04-16T17:51:05Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-04-16T17:51:05Z"
          },
          {
            "name": "Hong Kong",
            "updateDate": "2025-04-16T17:51:05Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-04-16T17:51:05Z"
          },
          {
            "name": "Protest and dissent",
            "updateDate": "2025-04-16T17:51:05Z"
          },
          {
            "name": "Rule of law and government transparency",
            "updateDate": "2025-04-16T17:51:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-03-21T14:42:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
    "originChamber": "Senate",
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
          "measure-id": "id119sres98",
          "measure-number": "98",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres98v00",
            "update-date": "2025-05-08"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution condemns China's Hong Kong national security law (officially called The Law of the People's Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region), the Hong Kong government's\u00a0Safeguarding National Security Ordinance, and related human rights abuses. The resolution also (1) supports the people of Hong Kong as they fight to exercise fundamental rights and freedoms; and (2) calls upon the Hong Kong government to drop all sedition and national security law-related charges and free all defendants immediately, including Jimmy Lai.</p>"
        },
        "title": "A resolution condemning Beijing's destruction of Hong Kong's democracy and rule of law."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres98.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution condemns China's Hong Kong national security law (officially called The Law of the People's Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region), the Hong Kong government's\u00a0Safeguarding National Security Ordinance, and related human rights abuses. The resolution also (1) supports the people of Hong Kong as they fight to exercise fundamental rights and freedoms; and (2) calls upon the Hong Kong government to drop all sedition and national security law-related charges and free all defendants immediately, including Jimmy Lai.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119sres98"
    },
    "title": "A resolution condemning Beijing's destruction of Hong Kong's democracy and rule of law."
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution condemns China's Hong Kong national security law (officially called The Law of the People's Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region), the Hong Kong government's\u00a0Safeguarding National Security Ordinance, and related human rights abuses. The resolution also (1) supports the people of Hong Kong as they fight to exercise fundamental rights and freedoms; and (2) calls upon the Hong Kong government to drop all sedition and national security law-related charges and free all defendants immediately, including Jimmy Lai.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119sres98"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres98is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres98rs.xml"
        }
      ],
      "type": "RS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution condemning Beijing's destruction of Hong Kong's democracy and rule of law.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:28Z"
    },
    {
      "title": "A resolution condemning Beijing's destruction of Hong Kong's democracy and rule of law.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-27T11:56:23Z"
    }
  ]
}
```
