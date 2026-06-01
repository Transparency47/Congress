# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2406?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2406
- Title: Canadian Snowbirds Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2406
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-11-19T12:03:18Z
- Update date including text: 2025-11-19T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2406",
    "number": "2406",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Canadian Snowbirds Act of 2025",
    "type": "S",
    "updateDate": "2025-11-19T12:03:18Z",
    "updateDateIncludingText": "2025-11-19T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T19:20:42Z",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "AZ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "AZ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2406is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2406\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Scott of Florida (for himself, Mr. Kelly , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Immigration and Nationality Act to authorize admission of Canadian retirees as long-term visitors for pleasure described in section 101(a)(15)(B) of such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Canadian Snowbirds Act of 2025 .\n#### 2. Admission of Canadian retirees\nSection 214 of the Immigration and Nationality Act ( 8 U.S.C. 1184 ) is amended by adding at the end the following:\n(s) Canadian retirees (1) In general The Secretary of Homeland Security may admit an alien as a visitor described in section 101(a)(15)(B) if the alien demonstrates, to the satisfaction of the Secretary, that the alien\u2014 (A) is a citizen of Canada; (B) is at least 50 years of age; (C) maintains a residence in Canada; (D) owns a residence in the United States or has signed a rental agreement for accommodations in the United States for the duration of the alien\u2019s intended stay in the United States; (E) is not inadmissible under section 212; (F) is not deportable under section 237; (G) is not otherwise removable under the immigration laws; (H) will not engage in employment or labor for hire in the United States other than employment or labor for hire for a person or entity not based in the United States by whom the Canadian citizen was employed in Canada or for whom the Canadian citizen performed services in Canada; and (I) will not seek any form of assistance, benefit, or credit described in section 403(a) of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1613(a) ) or sections 24(d), 32, 35, 36, and 36B of the Internal Revenue Code of 1986. (2) Spouse The spouse of an alien described in paragraph (1) may be admitted under the same terms as the principal alien if the spouse satisfies the requirements under paragraph (1) (other than subparagraph (D)). (3) Immigrant intent In determining eligibility for admission under this subsection, maintenance of a residence in the United States shall not be considered evidence of intent by the alien to abandon the alien\u2019s residence in Canada. (4) Period of admission During any single 365-day period, an alien may be admitted under this subsection as a visitor for pleasure described in section 101(a)(15)(B) for a period not to exceed 240 days, beginning on the date of admission. Time spent outside of the United States during such period of admission shall not be counted for purposes of determining the termination date of such period. (5) Secretary\u2019s discretion A decision by the Secretary of Homeland Security to withhold admission of an alien described in paragraph (1), or to withdraw an authorization of admission of such alien, shall be at the Secretary\u2019s sole and unreviewable discretion under the immigration laws. .\n#### 3. Nonresident alien tax status\nSubparagraph (B) of section 7701(b)(1) of the Internal Revenue Code of 1986 is amended by inserting , or, notwithstanding subparagraph (A)(ii), is a Canadian citizen described in section 214(s) of the Immigration and Nationality Act ( 8 U.S.C. 1184(s) ) after (within the meaning of subparagraph (A)) .",
      "versionDate": "2025-07-23",
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
        "name": "Immigration",
        "updateDate": "2025-09-17T16:40:44Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2406is.xml"
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
      "title": "Canadian Snowbirds Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Canadian Snowbirds Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to authorize admission of Canadian retirees as long-term visitors for pleasure described in section 101(a)(15)(B) of such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:28Z"
    }
  ]
}
```
