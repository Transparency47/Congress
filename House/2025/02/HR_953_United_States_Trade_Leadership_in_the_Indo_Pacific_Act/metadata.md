# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/953?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/953
- Title: United States Trade Leadership in the Indo-Pacific Act
- Congress: 119
- Bill type: HR
- Bill number: 953
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-04-09T15:15:14Z
- Update date including text: 2026-04-09T15:15:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/953",
    "number": "953",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "United States Trade Leadership in the Indo-Pacific Act",
    "type": "HR",
    "updateDate": "2026-04-09T15:15:14Z",
    "updateDateIncludingText": "2026-04-09T15:15:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:06:25Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NE"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "HI"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr953ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 953\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mrs. Miller of West Virginia (for herself, Mr. Panetta , Mr. Smith of Nebraska , Mr. Bera , Mr. LaHood , and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo advance United States long-term trade competitiveness and economic leadership in the Indo-Pacific region.\n#### 1. Short title\nThis Act may be cited as the United States Trade Leadership in the Indo-Pacific Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States is an Indo-Pacific power.\n**(2)**\nThe Indo-Pacific region, spanning from our Pacific Coastline to the Indian Ocean, is home to over half the world\u2019s people, including nearly 60 percent of youth, and is at the center of the 21st-century global economy, accounting for 60 percent of global gross domestic product and two-thirds of the world\u2019s economic growth in 2022.\n**(3)**\nThe Indo-Pacific region also includes some of America\u2019s closest military allies and partners, several of the world\u2019s largest militaries, and 5 nations allied with the United States through mutual defense treaties. The region also contains strategic rivals with growing military capabilities, in particular the People\u2019s Republic of China (PRC). Our partners are critical for responding to potential threats in the region, maintaining credible deterrence, and for fostering peace.\n**(4)**\nThere is broad bipartisan agreement that the United States must have a strong and durable economic strategy in the Indo-Pacific to advance our commercial, geostrategic, and national security interests and support our allies and partners in the region.\n**(5)**\nThis is especially true and increasingly urgent in the face of heightened aggression and pressure from the PRC, which seeks to expand its influence by actively pursuing trade agreements with key partners in the Indo-Pacific that establish preferential treatment for goods and services, deepen supply chain integration, and establish rules based on the PRC\u2019s state-led authoritarian economic model that undercut America\u2019s workers, businesses, and economic security.\n**(6)**\nFor decades, the United States has sought to persuade the PRC to eliminate harmful trade practices and act responsibly within the global rules-based trading system. Unfortunately, the PRC has not substantially changed its behavior and has instead used forced labor, subsidies and overproduction, intellectual property theft and the forced transfer of technology, authoritarian digital governance policies, economic coercion, and other unfair practices to advance an economic model that undermines human rights, American industries and workers, and market-based economies around the world.\n**(7)**\nThe PRC is now actively seeking to increase trade ties in the Indo-Pacific region as a means to increase its economic influence and increase supply chain dependency on the PRC. One of the most prominent examples of the PRC\u2019s growing economic influence in the Indo-Pacific region is the Regional Comprehensive Economic Partnership (RCEP), which entered into force in January 2022. RCEP is now the largest trade agreement in the world, encompassing 15 countries that account for 30 percent of the global economy. This agreement will increasingly put the United States at a competitive disadvantage as the economies of the PRC, Australia, Brunei, Cambodia, Indonesia, Japan, Korea, Laos, Malaysia, Myanmar, New Zealand, the Philippines, Singapore, Thailand, and Vietnam grow more integrated.\n**(8)**\nThe PRC is also actively negotiating numerous other regional and bilateral trade agreements throughout the region and is attempting to accede to the Comprehensive and Progressive Agreement for Trans-Pacific Partnership (CPTPP) as well as the Digital Economic Partnership Agreement (DEPA).\n**(9)**\nThe PRC\u2019s aggressive assertion of its economic interests in the Indo-Pacific through the use of trade agreements underscores the need for the United States to provide a meaningful and credible alternative to achieve our economic and national security goals.\n**(10)**\nAmerican workers and businesses also face competitive pressures as other countries in the region pursue regional rules and preferential trade agreements without the participation of the United States. There are now more than 200 preferential trade agreements in force with at least one party from the region and over 100 more are under negotiation or pending ratification.\n**(11)**\nTo inform future policymaking, Congress should work with the administration in a bipartisan manner to examine current United States economic policy toward the Indo-Pacific, the impacts of regional trade agreements on American competitiveness, and policies to advance United States objectives in the region.\n**(12)**\nThrough a more comprehensive trade and economic strategy toward the Indo-Pacific region, the United States could exert greater leverage to improve labor rights and help level the playing field for American workers, enhance environmental standards, counter non-market economies and authoritarianism, construct more resilient supply chains, better meet the needs of our allies and partners, and grow our economy by addressing barriers to trade for American products.\n#### 3. Investigation of impact of Indo-Pacific regional agreements on United States competitiveness\nNot later than 180 days after the date of the enactment of this Act, the United States International Trade Commission shall conduct and conclude an investigation to examine\u2014\n**(1)**\nhow preferential market access provisions, including tariffs, quotas, and services commitments, in existing Indo-Pacific regional trade agreements, including the Regional Comprehensive Economic Partnership (RCEP) Agreement and the Comprehensive and Progressive Agreement for Trans-Pacific Partnership (CPTPP), affect United States exports and growth opportunities in the Indo-Pacific region;\n**(2)**\nhow existing non-tariff barriers, including regulatory practices, relatively lower labor and environmental standards, different rules for sectors ranging from agriculture and the digital economy, and standard-setting in these areas as part of existing Indo-Pacific regional and bilateral trade agreements, impact the competitiveness of American workers and businesses;\n**(3)**\nthe impact of existing Indo-Pacific regional trade agreements on United States supply chain resiliency and connectivity, and in particular its impact on the People\u2019s Republic of China\u2019s role in key global supply chains; and\n**(4)**\ndifferences between the United States-Mexico-Canada Agreement (USMCA) and CPTPP, RCEP, or other regional trade agreements in the Indo-Pacific that would likely have a substantial impact on United States businesses and workers.\n#### 4. Indo-Pacific Trade Strategy Commission\n##### (a) Establishment\n**(1) In general**\nThere is hereby established an independent commission to be known as the Indo-Pacific Trade Strategy Commission (in this section referred to as the Commission ), to develop findings and recommendations for a comprehensive trade strategy for the Indo-Pacific region for purposes of\u2014\n**(A)**\nensuring sustained United States economic and geopolitical leadership in the Indo-Pacific region;\n**(B)**\npromoting United States innovation, exports, and economic opportunities for workers and businesses;\n**(C)**\ncountering the People\u2019s Republic of China\u2019s aggressive trade agenda;\n**(D)**\npromoting United States values, norms, and standards;\n**(E)**\nstrengthening the United States economy;\n**(F)**\nbolstering United States economic and national security, including by addressing the vulnerabilities identified in the G7 Leaders\u2019 Statement on Economic Resilience and Economic Security of May 20, 2023; and\n**(G)**\npromoting United States supply chain resilience.\n**(2) Effective date**\nThis subsection shall take effect on the date that is 30 days after the date of the enactment of this Act.\n##### (b) Membership\n**(1) Number and appointment**\nThe Commission shall be composed of 12 members appointed as follows:\n**(A)**\n6 members appointed by mutual agreement of the Chair of the Committee on Ways and Means of the House of Representatives and the Ranking Member of the Committee on Finance of the Senate.\n**(B)**\n6 members appointed by mutual agreement of the Chair of the Committee on Finance of the Senate and the Ranking Member of the Committee on Ways and Means of the House of Representatives.\n**(C)**\nNone of the appointed members shall be a Member of the House of Representatives or a Member of the Senate.\n**(2) Qualifications**\nThe members of the Commission shall be individuals who have well-documented expertise, knowledge, or experience in the Indo-Pacific region, and\u2014\n**(A)**\ninternational trade;\n**(B)**\neconomic and supply chain issues;\n**(C)**\nlabor matters; or\n**(D)**\nenvironmental policy.\n**(3) Meetings**\nThe Commission shall\u2014\n**(A)**\nhold public hearings and meetings;\n**(B)**\nhold classified hearings or meetings, if necessary to discuss classified material or information;\n**(C)**\nprovide an opportunity for public comment, including sharing of research and policy analysis, through publication of a solicitation for public comments during a period of not less than 45 days;\n**(D)**\nconsult quarterly with Congress, specifically with members of the Committee on Ways and Means of the House of Representatives and members of the Committee on Finance of the Senate; and\n**(E)**\nsubmit, not later than 18 months after the date of the enactment of this Act, a final report to Congress, specifically to the members of the Committee on Ways and Means of the House of Representatives and members of the Committee on Finance of the Senate.",
      "versionDate": "2025-02-04",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-06-26T15:43:29Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-06-26T15:43:24Z"
          },
          {
            "name": "Australia",
            "updateDate": "2025-06-26T15:44:37Z"
          },
          {
            "name": "Bangladesh",
            "updateDate": "2025-06-26T15:44:43Z"
          },
          {
            "name": "Bhutan",
            "updateDate": "2025-06-26T15:44:48Z"
          },
          {
            "name": "Brunei",
            "updateDate": "2025-06-26T15:44:53Z"
          },
          {
            "name": "Burma",
            "updateDate": "2025-06-26T15:44:57Z"
          },
          {
            "name": "Cambodia",
            "updateDate": "2025-06-26T15:45:01Z"
          },
          {
            "name": "China",
            "updateDate": "2025-06-26T15:43:18Z"
          },
          {
            "name": "Competitiveness, trade promotion, trade deficits",
            "updateDate": "2025-06-26T15:42:57Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-26T15:43:34Z"
          },
          {
            "name": "Fiji",
            "updateDate": "2025-06-26T15:45:07Z"
          },
          {
            "name": "Free trade and trade barriers",
            "updateDate": "2025-06-26T15:43:08Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-06-26T15:43:04Z"
          },
          {
            "name": "India",
            "updateDate": "2025-06-26T15:45:14Z"
          },
          {
            "name": "Indonesia",
            "updateDate": "2025-06-26T15:45:18Z"
          },
          {
            "name": "Japan",
            "updateDate": "2025-06-26T15:45:23Z"
          },
          {
            "name": "Kiribati",
            "updateDate": "2025-06-26T15:45:30Z"
          },
          {
            "name": "Laos",
            "updateDate": "2025-06-26T15:45:35Z"
          },
          {
            "name": "Malaysia",
            "updateDate": "2025-06-26T15:45:39Z"
          },
          {
            "name": "Maldives",
            "updateDate": "2025-06-26T15:45:55Z"
          },
          {
            "name": "Marshall Islands",
            "updateDate": "2025-06-26T15:46:00Z"
          },
          {
            "name": "Micronesia",
            "updateDate": "2025-06-26T15:46:08Z"
          },
          {
            "name": "Mongolia",
            "updateDate": "2025-06-26T15:46:13Z"
          },
          {
            "name": "Nauru",
            "updateDate": "2025-06-26T15:46:17Z"
          },
          {
            "name": "Nepal",
            "updateDate": "2025-06-26T15:46:22Z"
          },
          {
            "name": "New Zealand",
            "updateDate": "2025-06-26T15:46:28Z"
          },
          {
            "name": "North Korea",
            "updateDate": "2025-06-26T15:46:32Z"
          },
          {
            "name": "Oceania",
            "updateDate": "2025-06-26T15:48:05Z"
          },
          {
            "name": "Palau",
            "updateDate": "2025-06-26T15:46:38Z"
          },
          {
            "name": "Papua New Guinea",
            "updateDate": "2025-06-26T15:46:42Z"
          },
          {
            "name": "Philippines",
            "updateDate": "2025-06-26T15:46:47Z"
          },
          {
            "name": "Samoa",
            "updateDate": "2025-06-26T15:46:51Z"
          },
          {
            "name": "Singapore",
            "updateDate": "2025-06-26T15:46:55Z"
          },
          {
            "name": "Solomon Islands",
            "updateDate": "2025-06-26T15:47:02Z"
          },
          {
            "name": "South Asia",
            "updateDate": "2025-06-26T15:47:11Z"
          },
          {
            "name": "South Korea",
            "updateDate": "2025-06-26T15:47:17Z"
          },
          {
            "name": "Sri Lanka",
            "updateDate": "2025-06-26T15:47:22Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-09T15:15:14Z"
          },
          {
            "name": "Taiwan",
            "updateDate": "2025-06-26T15:47:26Z"
          },
          {
            "name": "Thailand",
            "updateDate": "2025-06-26T15:47:31Z"
          },
          {
            "name": "Tonga",
            "updateDate": "2025-06-26T15:47:39Z"
          },
          {
            "name": "Trade agreements and negotiations",
            "updateDate": "2025-06-26T15:43:13Z"
          },
          {
            "name": "Tuvalu",
            "updateDate": "2025-06-26T15:47:43Z"
          },
          {
            "name": "Vanuatu",
            "updateDate": "2025-06-26T15:47:49Z"
          },
          {
            "name": "Vietnam",
            "updateDate": "2025-06-26T15:47:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-05T14:51:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
    "originChamber": "House",
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
          "measure-id": "id119hr953",
          "measure-number": "953",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr953v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>United States Trade Leadership in the Indo-Pacific Act</strong></p><p>This bill requires certain actions related to trade in the Indo-Pacific region.</p><p>Specifically, the bill directs the U.S. International Trade Commission to investigate the effects of existing Indo-Pacific regional trade agreements (e.g., the Regional Comprehensive Economic Partnership and the Comprehensive and Progressive Agreement for Trans-Pacific Partnership) on U.S. exporters and competitiveness in the region.</p><p>Additionally, the bill establishes the Indo-Pacific Trade Strategy Commission to develop findings and recommendations for a comprehensive trade strategy for the Indo-Pacific region.</p>"
        },
        "title": "United States Trade Leadership in the Indo-Pacific Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr953.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Trade Leadership in the Indo-Pacific Act</strong></p><p>This bill requires certain actions related to trade in the Indo-Pacific region.</p><p>Specifically, the bill directs the U.S. International Trade Commission to investigate the effects of existing Indo-Pacific regional trade agreements (e.g., the Regional Comprehensive Economic Partnership and the Comprehensive and Progressive Agreement for Trans-Pacific Partnership) on U.S. exporters and competitiveness in the region.</p><p>Additionally, the bill establishes the Indo-Pacific Trade Strategy Commission to develop findings and recommendations for a comprehensive trade strategy for the Indo-Pacific region.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr953"
    },
    "title": "United States Trade Leadership in the Indo-Pacific Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Trade Leadership in the Indo-Pacific Act</strong></p><p>This bill requires certain actions related to trade in the Indo-Pacific region.</p><p>Specifically, the bill directs the U.S. International Trade Commission to investigate the effects of existing Indo-Pacific regional trade agreements (e.g., the Regional Comprehensive Economic Partnership and the Comprehensive and Progressive Agreement for Trans-Pacific Partnership) on U.S. exporters and competitiveness in the region.</p><p>Additionally, the bill establishes the Indo-Pacific Trade Strategy Commission to develop findings and recommendations for a comprehensive trade strategy for the Indo-Pacific region.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr953"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr953ih.xml"
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
      "title": "United States Trade Leadership in the Indo-Pacific Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States Trade Leadership in the Indo-Pacific Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To advance United States long-term trade competitiveness and economic leadership in the Indo-Pacific region.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:35Z"
    }
  ]
}
```
