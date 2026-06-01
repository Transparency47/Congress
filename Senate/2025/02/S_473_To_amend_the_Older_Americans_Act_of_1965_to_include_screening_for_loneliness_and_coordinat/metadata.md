# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/473?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/473
- Title: SENIOR Act
- Congress: 119
- Bill type: S
- Bill number: 473
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-05-27T14:12:56Z
- Update date including text: 2025-05-27T14:12:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/473",
    "number": "473",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
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
    "title": "SENIOR Act",
    "type": "S",
    "updateDate": "2025-05-27T14:12:56Z",
    "updateDateIncludingText": "2025-05-27T14:12:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T22:05:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MN"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s473is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 473\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Scott of Florida (for himself, Ms. Smith , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Older Americans Act of 1965 to include screening for loneliness and coordination of supportive services and health care to address the negative health effects of loneliness, to require a report on loneliness, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Social Engagement and Network Initiatives for Older Relief Act or the SENIOR Act .\n#### 2. Screening older individuals for loneliness and coordination of supportive services and health care to address loneliness\nSection 102(14)(N) of the Older Americans Act of 1965 ( 42 U.S.C. 3002(14)(N) ) is amended by inserting and loneliness after social isolation each place it appears.\n#### 3. Report on loneliness\n##### (a) Preparation of report\n**(1) In general**\nThe Secretary shall, in carrying out activities under section 206(a) of the Older Americans Act of 1965 ( 42 U.S.C. 3017(a) ), prepare a report\u2014\n**(A)**\non programs authorized by such Act ( 42 U.S.C. 3001 et seq. ), and supported or funded by the Administration on Aging, that include a focus on addressing the negative health effects associated with loneliness through targeting older individuals identified as being in greatest social need, as appropriate; and\n**(B)**\nthat examines the relationship between the strength of multigenerational family units and loneliness in older individuals.\n**(2) Impact**\nSuch report shall identify\u2014\n**(A)**\nwhether loneliness is being adequately addressed under the programs described in paragraph (1)(A), including, to the extent practicable\u2014\n**(i)**\nthe prevalence of loneliness across geographic areas;\n**(ii)**\nthe negative physical and mental health effects associated with loneliness; and\n**(iii)**\nthe role of preventive measures and services under this Act in addressing the negative health effects associated with loneliness among older individuals; and\n**(B)**\npublic awareness of and efforts to address the negative health effects associated with loneliness.\n**(3) Types of programs**\nSuch report shall identify whether programs described in paragraph (1)(A)\u2014\n**(A)**\nsupport projects in local communities and involve diverse sectors associated with such communities to decrease the negative health effects associated with loneliness among older individuals and caregivers;\n**(B)**\nsupport outreach activities to screen older individuals for negative health effects associated with loneliness; and\n**(C)**\ninclude a focus on decreasing the negative health effects associated with loneliness.\n**(4) Recommendations**\nSuch report shall, as appropriate, include\u2014\n**(A)**\nrecommendations for reducing the negative health effects associated with loneliness and to address any negative health effects identified under clauses (ii) and (iii) of subparagraph (A), and subparagraph (B), of paragraph (2); and\n**(B)**\nrecommendations for policies or programs that foster strong and stable connections across different generations in a family.\n##### (b) Submission of report\n**(1) Interim status report**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall submit an interim report, to the committees of the Senate and of the House of Representatives with jurisdiction over the Older Americans Act of 1965 ( 42 U.S.C. 3001 et seq. ), and the Special Committee on Aging of the Senate, on the status of the evaluation underway to develop the final report required under this section.\n**(2) Final report**\nNot later than 5 years after the date of enactment of this Act, the Secretary shall submit a final report that meets the requirements of this section to the committees of the Senate and of the House of Representatives with jurisdiction over the Older Americans Act of 1965 ( 42 U.S.C. 3001 et seq. ) and the Special Committee on Aging of the Senate.\n##### (c) Definitions\nFor purposes of this section, the terms greatest social need , older individual , and Secretary have the meanings given such terms in section 102 of the Older Americans Act of 1965 ( 42 U.S.C. 3002 ).",
      "versionDate": "2025-02-06",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Aging",
            "updateDate": "2025-04-24T16:06:44Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-04-24T16:07:11Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-24T16:06:58Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-24T16:07:03Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-04-24T16:07:19Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-24T16:06:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T16:25:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s473",
          "measure-number": "473",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-05-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s473v00",
            "update-date": "2025-05-05"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Social Engagement and Network Initiatives for Older Relief Act or the SENIOR Act</strong></p><p>This bill expands the scope of authorized\u00a0Administration on Aging (AOA) grants to include\u00a0services addressing loneliness in older individuals (i.e., aged 60 or older), and requires a report evaluating whether certain federal programs are adequately addressing this topic.</p><p>Under current law, the\u00a0AOA provides grants to states for disease prevention and health promotion services for older individuals, including services addressing the negative health effects of social isolation.\u00a0The bill expands the scope of the services eligible for\u00a0these grants to include services addressing the negative health effects of loneliness.</p><p>Also, the bill requires the Department of Health and Human Services to submit to Congress a report (1)\u00a0evaluating whether its programs for older individuals\u00a0are adequately addressing loneliness,\u00a0and (2)\u00a0recommending measures for reducing the negative health effects of loneliness and fostering multigenerational family connections.\u00a0</p>"
        },
        "title": "SENIOR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s473.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Social Engagement and Network Initiatives for Older Relief Act or the SENIOR Act</strong></p><p>This bill expands the scope of authorized\u00a0Administration on Aging (AOA) grants to include\u00a0services addressing loneliness in older individuals (i.e., aged 60 or older), and requires a report evaluating whether certain federal programs are adequately addressing this topic.</p><p>Under current law, the\u00a0AOA provides grants to states for disease prevention and health promotion services for older individuals, including services addressing the negative health effects of social isolation.\u00a0The bill expands the scope of the services eligible for\u00a0these grants to include services addressing the negative health effects of loneliness.</p><p>Also, the bill requires the Department of Health and Human Services to submit to Congress a report (1)\u00a0evaluating whether its programs for older individuals\u00a0are adequately addressing loneliness,\u00a0and (2)\u00a0recommending measures for reducing the negative health effects of loneliness and fostering multigenerational family connections.\u00a0</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119s473"
    },
    "title": "SENIOR Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Social Engagement and Network Initiatives for Older Relief Act or the SENIOR Act</strong></p><p>This bill expands the scope of authorized\u00a0Administration on Aging (AOA) grants to include\u00a0services addressing loneliness in older individuals (i.e., aged 60 or older), and requires a report evaluating whether certain federal programs are adequately addressing this topic.</p><p>Under current law, the\u00a0AOA provides grants to states for disease prevention and health promotion services for older individuals, including services addressing the negative health effects of social isolation.\u00a0The bill expands the scope of the services eligible for\u00a0these grants to include services addressing the negative health effects of loneliness.</p><p>Also, the bill requires the Department of Health and Human Services to submit to Congress a report (1)\u00a0evaluating whether its programs for older individuals\u00a0are adequately addressing loneliness,\u00a0and (2)\u00a0recommending measures for reducing the negative health effects of loneliness and fostering multigenerational family connections.\u00a0</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119s473"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s473is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Older Americans Act of 1965 to include screening for loneliness and coordination of supportive services and health care to address the negative health effects of loneliness, to require a report on loneliness, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:24Z"
    },
    {
      "title": "SENIOR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SENIOR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Social Engagement and Network Initiatives for Older Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    }
  ]
}
```
