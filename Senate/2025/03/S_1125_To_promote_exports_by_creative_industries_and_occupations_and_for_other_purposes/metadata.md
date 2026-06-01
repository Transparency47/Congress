# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1125?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1125
- Title: Cultural Trade Promotion Act
- Congress: 119
- Bill type: S
- Bill number: 1125
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-05-27T14:12:52Z
- Update date including text: 2025-05-27T14:12:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1125",
    "number": "1125",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001194",
        "district": "",
        "firstName": "Brian",
        "fullName": "Sen. Schatz, Brian [D-HI]",
        "lastName": "Schatz",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Cultural Trade Promotion Act",
    "type": "S",
    "updateDate": "2025-05-27T14:12:52Z",
    "updateDateIncludingText": "2025-05-27T14:12:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T19:56:52Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1125is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1125\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Schatz (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo promote exports by creative industries and occupations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cultural Trade Promotion Act .\n#### 2. Definitions\nIn this Act:\n**(1) Creative industry or occupation**\nThe term creative industry or occupation means\u2014\n**(A)**\nan industry that\u2014\n**(i)**\nhas a substantial current or potential impact (including through positions that lead to economic self-sufficiency and opportunities for advancement) on a State, regional, or local economy or a Native American community's economy, as appropriate; and\n**(ii)**\ncontributes to the growth of businesses, nonprofit organizations, or self-employment opportunities that have their origin in individual creativity, skill, and talent, including such businesses, organizations, or opportunities focused on design, crafts, music, visual and media arts, performing arts, language, literature, or expressions of Native cultures or regional or local heritage culture; and\n**(B)**\nan occupation that\u2014\n**(i)**\ncurrently has or is projected to have a number of positions (including positions that lead to economic self-sufficiency and opportunities for advancement) in an industry sector so as to have a substantial potential impact on a State, regional, or local economy or a Native American community's economy, as appropriate; and\n**(ii)**\nis comprised of\u2014\n**(I)**\nbusinesses or nonprofit organizations described in subparagraph (A)(ii); or\n**(II)**\nindividuals who are self-employed or sole proprietors and whose work has an origin in individual creativity, skill, and talent, including a focus on design, crafts, music, visual arts, media arts, performing arts, language, literature, or expressions of Native cultures or regional or local heritage culture.\n**(2) Native American**\nThe term Native American , used with respect to culture, means the culture of a Native American, as defined in section 103 of the Native American Languages Act ( 25 U.S.C. 2902 ).\n#### 3. Promotion of exports from microenterprises and creative industries and occupations\n##### (a) Promotion of exports by United States and Foreign Commercial Service\nSection 2301(b) of the Export Enhancement Act of 1988 ( 15 U.S.C. 4721(b) ) is amended, in the matter preceding paragraph (1), by striking small businesses and medium-sized businesses and inserting microentrepreneurs (as defined in section 172 of the Program for Investment in Microentrepreneurs Act of 1999 ( 15 U.S.C. 6901 )), small businesses, and medium-sized businesses .\n##### (b) Strategic plan of Trade Promotion Coordinating Committee\nSection 2312(c) of the Export Enhancement Act of 1988 ( 15 U.S.C. 4727(c) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (7)\u2014\n**(A)**\nby inserting microenterprises (as defined in section 172 of the Program for Investment in Microentrepreneurs Act of 1999 ( 15 U.S.C. 6901 )) and after better assist ; and\n**(B)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(8) consider how to promote exports of goods and services from creative industries and occupations (as defined in section 2 of the Cultural Trade Promotion Act ). .\n##### (c) Promotion of exports of Native Hawaiian arts and crafts and exports from Native Hawaiian owned-Businesses\nSection 2307 of the Export Enhancement Act of 1988 ( 15 U.S.C. 4726 ) is amended\u2014\n**(1)**\nby inserting or Native Hawaiian after American Indian each place it appears;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby inserting or Native Hawaiian after include Indian ; and\n**(B)**\nby inserting or Native Hawaiian-owned after Indian-owned ; and\n**(3)**\nin subsection (e), by striking hand made or hand crafted and inserting made .\n#### 4. Collaboration to improve access to reliable international shipping services\nThe Under Secretary of Commerce for International Trade, the Assistant Secretary of Commerce and Director General of the United States and Foreign Commercial Service appointed under section 2301(a)(2) of the Export Enhancement Act of 1988 ( 15 U.S.C. 4721(a)(2) ), and the Postmaster General shall consult and collaborate with respect to how to better connect microenterprises (as defined in section 172 of the Program for Investment in Microentrepreneurs Act of 1999 ( 15 U.S.C. 6901 )) and small businesses to fast, reliable international shipping services that meet the expectations of the modern consumer.\n#### 5. Focus on creative industries and occupations by Trade and Development Agency\nSection 661(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2421(a) ) is amended in the second sentence by striking and environment and inserting environment, and creative industries and occupations (as defined in section 2 of the Cultural Trade Promotion Act ) .\n#### 6. Travel and tourism advisory board\nNotwithstanding any other provision of law (including any regulation), the Secretary of Commerce shall appoint to serve as a permanent member of the United States Travel and Tourism Advisory Board established pursuant to section 3 of the Act of February 14, 1903 ( 15 U.S.C. 1512 ; 32 Stat. 826, chapter 552), and chapter 10 of title 5, United States Code, a representative of creative industries and occupations.",
      "versionDate": "2025-03-25",
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
        "updateDate": "2025-05-12T18:11:48Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1125is.xml"
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
      "title": "Cultural Trade Promotion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T01:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Cultural Trade Promotion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote exports by creative industries and occupations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:34Z"
    }
  ]
}
```
