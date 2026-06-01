# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8025?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8025
- Title: Protecting American Streaming and Innovation Act
- Congress: 119
- Bill type: HR
- Bill number: 8025
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-16T08:07:03Z
- Update date including text: 2026-04-16T08:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8025",
    "number": "8025",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Protecting American Streaming and Innovation Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:07:03Z",
    "updateDateIncludingText": "2026-04-16T08:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "FL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "NY"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "TX"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "PA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "WV"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "IN"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "KS"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8025ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8025\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Smucker (for himself, Mr. Steube , Ms. Malliotakis , Mr. Moran , Mr. Kelly of Pennsylvania , and Mrs. Miller of West Virginia ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide for an investigation of Canadian digital trade practices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting American Streaming and Innovation Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nDigital trade is a critical engine of the United States economy, allowing American companies to deliver innovative audiovisual and audio products and services globally, creating high-paying jobs in the United States and exporting American culture and values.\n**(2)**\nThe United States-Mexico-Canada Agreement (USMCA), which entered into force on July 1, 2020, includes a robust digital trade chapter intended to prevent discriminatory barriers and ensure a level playing field for North American digital service providers.\n**(3)**\nCanada\u2019s law, the Online Streaming Act, empowers Canadian regulators to apply contribution and discoverability obligations to audio and audio-visual content, resulting in a revenue-based tax that targets American companies.\n**(4)**\nCanada has chosen to exempt domestic streaming companies from these obligations, while applying strict obligations to U.S.-based companies. The contribution obligations currently require U.S. companies to pay mandatory high-percentage contributions based on models derived from traditional broadcasters and direct these funds exclusively to domestic cultural funds. They also require U.S. audio streaming companies to pay twice because royalties paid by audio services to Canadian rightsholders are included in services\u2019 taxable revenue. Discoverability obligations potentially require U.S. companies to undertake costly and technically burdensome platform modifications, including the implementation of invasive data collection and reporting systems, to enforce content prioritization or quotas. These obligations are discriminatory and place a disproportionate burden on United States commerce.\n**(5)**\nThese measures appear to contravene Canada\u2019s commitments under the USMCA to provide non-discriminatory treatment to United States digital products and services and avoid unnecessary barriers to digital trade, and appear to be unreasonable, discriminatory, and excessively burdensome towards United States commerce. These measures also appear to be a prohibited performance requirement.\n**(6)**\nCanada has invoked the USMCA cultural industries exception to defend measures like the Online Streaming Act that affect audiovisual and music services. However, the exception traces to the Canada-U.S. Free Trade Agreement era and retains a legacy definition of cultural industry centered on traditional publishing, recordings, and broadcasting, rather than modern means of digital delivery.\n**(7)**\nIf left unchecked, Canada\u2019s discriminatory digital policies will set a harmful global precedent, encouraging other nations to adopt similar protectionist digital sovereignty regimes that target successful United States streaming companies and content producers. Trading partners such as Australia, Brazil, Israel, and others have adopted or are considering similar discriminatory digital policies that primarily impact U.S.-based services. Additionally, even within Canada, Quebec is considering an overlapping regime targeting United States companies.\n**(8)**\nIt is in the national economic interest of the United States to enforce its rights under trade agreements and statutory authorities and take appropriate action to address foreign practices that are unreasonable, discriminatory, and burden or restrict United States commerce.\n#### 3. Investigation of Canadian digital trade practices\n##### (a) In general\nNot later than 30 days after the date of the enactment of this Act, the United States Trade Representative shall initiate an investigation under section 301 of the Trade Act of 1974 ( 19 U.S.C. 2411 ) to determine whether Canada\u2019s implementation of its Online Streaming Act (Bill C-11), including the related regulatory actions of the Canadian Radio-television and Telecommunications Commission (CRTC), constitutes an act, policy, or practice that is unreasonable or discriminatory and burdens or restricts United States commerce.\n##### (b) Consultations\nIn conducting the investigation required by subsection (a), the Trade Representative shall\u2014\n**(1)**\nconsult with affected United States businesses providing online audiovisual or audio streaming services;\n**(2)**\nseek information from relevant trade associations, labor representatives, and cultural organizations; and\n**(3)**\ncoordinate with the Department of Commerce, the Department of State, and the United States International Trade Commission.\n##### (c) Determinations and action\n**(1) Affirmative determination**\nIf the Trade Representative makes an affirmative determination under subsection (a), the Trade Representative shall\u2014\n**(A)**\npublish such determination in the Federal Register; and\n**(B)**\nconsider appropriate action under section 301(c) of the Trade Act of 1974 ( 19 U.S.C. 2411(c) ), which may include the suspension of trade agreement benefits or imposition of duties commensurate with the burden imposed.\n**(2) Negative determination**\nIf the Trade Representative makes a negative determination under subsection (a) and determines that no action described in paragraph (1)(B) is warranted, the Trade Representative shall transmit to the appropriate congressional committees a report explaining the determination.\n#### 4. Reporting requirements\n##### (a) Initial report\nNot later than 90 days after the date of the enactment of this Act, the United States Trade Representative shall submit to the appropriate congressional committees a report on\u2014\n**(1)**\nthe implementation of the requirements of section 3;\n**(2)**\nCanada\u2019s regulatory implementation schedule for the Online Streaming Act (Bill C-11); and\n**(3)**\nthe preliminary findings on the impact of these measures on United States digital service providers.\n##### (b) Quarterly updates\nThe Trade Representative shall submit updates to the report required by subsection (a) on a quarterly basis for a period of two years describing\u2014\n**(1)**\nconsultations held with affected stakeholders;\n**(2)**\nany remedial or enforcement actions undertaken; and\n**(3)**\nthe state of bilateral engagement with Canada on digital trade issues.\n##### (c) Public summary\nThe Trade Representative shall make publicly available a non-confidential summary of each report and update submitted under this section.\n#### 5. Retaliatory actions if Canada fails to remedy discriminatory measures\n##### (a) Determination of non-Compliance\nIf, not later than 180 days after publication of an affirmative determination under section 3(c)(1), the United States Trade Representative determines that Canada has not taken satisfactory steps to remove or amend the discriminatory measures identified in the investigation with respect to which the determination was made, the Trade Representative shall take appropriate action under section 301(c) of the Trade Act of 1974 ( 19 U.S.C. 2411(c) ).\n##### (b) Forms of action\nActions under subsection (a) may include\u2014\n**(1)**\nthe suspension, withdrawal, or modification of trade agreement concessions or benefits to Canada under the United States-Mexico-Canada Agreement or other agreements; and\n**(2)**\nthe imposition of additional duties on goods of Canadian origin in amounts commensurate with the harm from implementation of Canada\u2019s Online Streaming Act (Bill C-11).\n##### (c) Notice and consultation\nBefore taking any action under this section, the Trade Representative shall\u2014\n**(1)**\nnotify the appropriate congressional committees of the proposed action; and\n**(2)**\nconsult with affected stakeholders to ensure that measures are targeted, proportionate, and minimize unintended consequences for United States consumers and allies.\n##### (d) Termination of action\nThe Trade Representative may terminate any action under this section if\u2014\n**(1)**\nCanada eliminates or modifies the measures to the satisfaction of the Trade Representative; and\n**(2)**\nthe Trade Representative notifies Congress in writing thereof.\n#### 6. Relation to other global free trade agreements\nTo the extent that any other foreign country with which the United States has in effect a free trade agreement takes actions that are similar to the actions of Canada described in section 3(a), the Trade Representative shall apply the provisions of sections 3, 4, and 5 to such other foreign country.\n#### 7. Definitions\nIn this Act\u2014\n**(1)**\nthe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Ways and Means of the House of Representatives; and\n**(B)**\nthe Committee on Finance of the Senate; and\n**(2)**\nthe term online streaming service means any digital service delivering audiovisual or audio programming to users in Canada via the internet.",
      "versionDate": "2026-03-19",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-04-09T14:27:47Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8025ih.xml"
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
      "title": "Protecting American Streaming and Innovation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T12:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting American Streaming and Innovation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T12:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for an investigation of Canadian digital trade practices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T12:03:41Z"
    }
  ]
}
```
