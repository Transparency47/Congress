# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3978?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3978
- Title: Investments in Rural Transit Act
- Congress: 119
- Bill type: S
- Bill number: 3978
- Origin chamber: Senate
- Introduced date: 2026-03-03
- Update date: 2026-04-21T19:18:51Z
- Update date including text: 2026-04-21T19:18:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in Senate
- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-03-03: Introduced in Senate

## Actions

- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3978",
    "number": "3978",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Investments in Rural Transit Act",
    "type": "S",
    "updateDate": "2026-04-21T19:18:51Z",
    "updateDateIncludingText": "2026-04-21T19:18:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T22:32:10Z",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "SD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3978is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3978\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2026 Ms. Smith (for herself, Mr. Rounds , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo increase the Federal operating share for rural transit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Investments in Rural Transit Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administration**\nThe term Administration means the Federal Transit Administration.\n**(2) Administrator**\nThe term Administrator means the Administrator of the Administration.\n**(3) Rural area**\nThe term rural area has the meaning given the term in section 5302 of title 49, United States Code.\n**(4) Secretary**\nThe term Secretary means the Secretary of Transportation.\n#### 3. Procurement streamlining\n##### (a) Expansion\nSection 3019(b) of the FAST Act ( 49 U.S.C. 5325 note) is amended\u2014\n**(1)**\nin paragraph (1)(A)\u2014\n**(A)**\nin clause (i)(I), by inserting or local after State ;\n**(B)**\nin clause (ii), by striking subclauses (I) and (II) and inserting the following:\n(I) a nonprofit cooperative purchasing organization that is not a grantee; (II) a consortium of grantees; or (III) a consortium of entities described in subclause (I); ;\n**(C)**\nin clause (iii), by inserting or local after State ; and\n**(D)**\nby amending clause (v) to read as follows:\n(v) the term participate means to purchase or procure under a cooperative procurement contract, using assistance provided under chapter 53 of title 49, United States Code\u2014 (I) rolling stock and related equipment; (II) farebox equipment, software or technology; or (III) other equipment or technology eligible for assistance under that chapter. ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the paragraph heading, by inserting government, local government, or eligible nonprofit entity after State ;\n**(B)**\nby inserting , local government, or eligible nonprofit entity after State government each place that term appears; and\n**(C)**\nby inserting or other equipment or technology eligible under chapter 53 of title 49, United States Code, after related equipment each place that term appears.\n##### (b) Recommendations\nThe Secretary, acting through the Administrator, shall\u2014\n**(1)**\nestablish a process to solicit feedback from grantees, State departments of transportation, and other relevant parties for improving and streamlining joint procurement and cooperative procurement and other strategies for improving rolling stock procurement and other procurements;\n**(2)**\nassess the feedback solicited under paragraph (1) and make advisory recommendations to improve and streamline\u2014\n**(A)**\njoint procurement;\n**(B)**\ncooperative procurement; or\n**(C)**\nother procurement strategies for rolling stock; and\n**(3)**\nsubmit to Congress and make publicly available on the website of the Administration annual reports on advisory recommendations concerning procurement, including recommended statutory, regulatory, and or guidance changes and potential cost savings.\n#### 4. Amendments to mass transit\n##### (a) In general\nChapter 53 of title 49, United States Code, is amended\u2014\n**(1)**\nin section 5311\u2014\n**(A)**\nin subsection (g)(2)\u2014\n**(i)**\nby striking assistance and all that follows through subparagraph (B), a and inserting assistance .\u2014A ;\n**(ii)**\nby striking 50 and inserting 80 ; and\n**(iii)**\nby striking subparagraph (B); and\n**(B)**\nby adding at the end the following:\n(k) Regulatory relief The Secretary, acting through the Administrator of the Federal Transit Administration, shall establish a process to make recommendations to the Administrator regarding regulatory relief for recipients of assistance under this section, which shall include input from rural transit agencies, Tribal transit agencies, State departments of transportation, and other relevant parties. ; and\n**(2)**\nin section 5339(b), by adding at the end the following:\n(12) Tribal projects (A) In general Subject to subparagraph (B), not less than 5 percent of the amounts made available under this subsection in a fiscal year shall be distributed to Tribal transit agencies. (B) Unutilized amounts The Secretary may use less than 5 percent of the amounts made available under this subsection in a fiscal year for the projects described in subparagraph (A) if the Secretary cannot meet the requirements of that subparagraph due to insufficient eligible applications. (C) Government share of costs The Federal share of the cost of an eligible project carried out under this subsection shall be up to 100 percent. .\n#### 5. Associate Administrator for Program Management and Tribal Transit\nNot later than1 year after the date of enactment of this Act, the Secretary shall designate an Associate Administrator for Program Management and Tribal Transit within the Administration, who shall, in addition to any responsibilities assigned by the Secretary or the Administrator, focus on capacity-building, coordination, and technical assistance for Tribal transit.\n#### 6. Joint review on low- to no-emission procurement opportunities in rural areas\nNot later than 2 years after the date of enactment of this Act, the Secretary and the Secretary of Energy shall consult with rural transit agencies, Tribal transit agencies, and other relevant parties and issue a publicly available joint report on opportunities to make the procurement of low- and no-emission infrastructure by rural transit agencies more efficient, in particular opportunities to collaborate with other public entities in the community, including school districts and municipalities.",
      "versionDate": "2026-03-03",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-21T19:18:51Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3978is.xml"
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
      "title": "Investments in Rural Transit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Investments in Rural Transit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase the Federal operating share for rural transit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T03:18:30Z"
    }
  ]
}
```
