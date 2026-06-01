# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2424?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2424
- Title: THINK TWICE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2424
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2026-01-20T19:52:11Z
- Update date including text: 2026-01-20T19:52:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 238.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 238.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2424",
    "number": "2424",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "THINK TWICE Act of 2025",
    "type": "S",
    "updateDate": "2026-01-20T19:52:11Z",
    "updateDateIncludingText": "2026-01-20T19:52:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 238.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-30",
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
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
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
        "item": [
          {
            "date": "2025-10-30T15:18:42Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:03:45Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-23T22:18:40Z",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CO"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2424is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2424\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Ricketts (for himself and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require a report of, and a strategy to combat, arms sales of the Government of the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tracking Hostile Industry Networks and Kit while Thwarting Weapons Imports from Chinese Entities Act of 2025 or the THINK TWICE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe People's Republic of China is the fourth largest arms exporter behind the United States, the Russian Federation, and France.\n**(2)**\nArms sales by entities in the People's Republic of China are an important element of the country's growing military power and geopolitical influence.\n**(3)**\nThe People's Republic of China uses arms sales to promote strategic interests, including\u2014\n**(A)**\nimproving the image and reputation of the People\u2019s Liberation Army;\n**(B)**\nacquiring performance data of Chinese-made weapons in contested environments, which can be utilized by the People's Liberation Army;\n**(C)**\nexacerbating tensions between the United States and traditional security partners;\n**(D)**\ngaining a foothold for further defense and security cooperation with certain countries;\n**(E)**\nbuilding relationships with senior political and military leaders in other countries, further expanding the diplomatic and strategic influence of the People\u2019s Republic of China;\n**(F)**\nprotecting economic interests of the People's Republic of China by ensuring the security of foreign partner governments to safeguard Chinese investments and Chinese workers;\n**(G)**\nexerting influence over the progression of conflicts to serve the broader geostrategic aims of the People's Republic of China;\n**(H)**\nimproving military operations and capabilities of partner states, thereby stabilizing regions of interest by addressing local issues, such as disturbances near the border of the People's Republic of China; and\n**(I)**\nsubsidizing the research and development and production costs of weapons systems of the People's Republic of China.\n#### 3. Report on arms sales of the People's Republic of China\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the Secretary of Defense, in coordination with the Secretary of State, shall submit to the appropriate congressional committees a report on arms sales facilitated by entities in the People\u2019s Republic of China.\n##### (b) Contents\nThe report required by subsection (a) shall include an analysis of\u2014\n**(1)**\nthe weapons systems and defense equipment originating from the People's Republic of China available for purchase;\n**(2)**\nthe technical aspects and capabilities of such weapons systems and defense equipment;\n**(3)**\nhow such weapons systems and defense equipment may impact the balance of power in the area of responsibility of each United States Combatant Command, when applicable;\n**(4)**\nthe weapons systems and defense equipment originating from the People's Republic of China that are considered direct alternatives to weapons systems and defense equipment originating from the United States;\n**(5)**\nthe weapons systems and defense equipment originating from the People\u2019s Republic of China that present the greatest security risks regarding the potential to collect intelligence on or compromise assets, weapons, or platforms of the United States;\n**(6)**\nthe countries mostly likely to procure weapons systems and defense equipment originating from the People's Republic of China, including the specific type, quantity, and estimated value in United States dollars of weapons, during the 1-year period following the date of the submission of the report;\n**(7)**\nthe weapons systems and defense equipment in development as of the date of the submission of the report by entities in the People's Republic of China that could be available on the global market not later than 5 years after such date;\n**(8)**\nthe factors that incentivize countries to procure such weapons systems and defense equipment, including costs, flexible payment conditions and financing, a lack of end-user agreements, and speed of sale and delivery; and\n**(9)**\nthe strategy of the People's Republic of China regarding arms sales and variables that could influence such strategy.\n##### (c) Form\n**(1) In general**\nThe report required by subsection (a) shall be submitted in unclassified form, but shall include a classified annex.\n**(2) Classified annex**\nThe classified annex required by paragraph (1) shall contain\u2014\n**(A)**\nan assessment by the National Intelligence Council of the contents required by subsection (b); and\n**(B)**\nan assessment by the Director of National Intelligence of the counterintelligence risks and risks of onward proliferation of technology and defense systems originating in the United States and created through the purchase, deployment, and use of weapons systems and defense equipment originating from the People\u2019s Republic of China by United States allies and partners.\n##### (d) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Armed Services, the Committee on Foreign Relations, and the Select Committee on Intelligence of the Senate; and\n**(2)**\nthe Committee on Armed Services, the Committee on Foreign Affairs, and the Permanent Select Committee on Intelligence of the House of Representatives.\n#### 4. Strategy to combat arms sales of the People's Republic of China\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Defense, shall develop a strategy to dissuade purchases of new weapons systems and defense equipment, excluding spare parts or parts for maintenance of previously procured weapons, originating from the People's Republic of China.\n##### (b) Elements\nThe strategy shall include the following elements:\n**(1)**\nAn information campaign targeting countries interested in procuring weapons systems and defense equipment originating from the People's Republic of China to warn such countries about\u2014\n**(A)**\npotential risks, including the lack of a proven track record in combat, insufficient training on the operation of the weapon or weapons system, reliability issues, and the lack of maintenance and spare parts available;\n**(B)**\nthe inability to integrate such weapons systems and defense equipment with weapons systems and defense equipment from the United States; and\n**(C)**\nthe potential limitation of future security cooperation with the United States that could arise if such weapons are acquired.\n**(2)**\nA description of actions the United States can take, including reforms to the foreign military sales, direct commercial sales, and foreign military financing processes, to make weapons systems and defense equipment from the United States more attractive to prospective buyers of weapons systems or defense equipment originating from the People's Republic of China.\n**(3)**\nA description of actions defense firms of the United States can take to provide competitive alternatives to prospective buyers of weapons systems and defense equipment originating from the People's Republic of China.\n**(4)**\nAn analysis of whether the use of sanctions, export controls, or other economic restrictions targeting buyers of new weapons systems or defense equipment originating from the People\u2019s Republic of China could serve as an effective deterrent.\n**(5)**\nA plan to ensure sufficient representation of defense firms of the United States, or trusted allies, at defense expositions where defense firms of the People\u2019s Republic of China are also attending.\n**(6)**\nA plan to combat Chinese disinformation campaigns targeting the performance of weapons or platforms produced by the United States or trusted allies.\n**(7)**\nA plan to ensure close coordination with Congress to prevent disjointed engagement with countries.\n##### (c) Report and implementation plan\nNot later than the date on which the strategy required by subsection (a) is completed, the Secretary of State shall submit to the appropriate congressional committees a report detailing the strategy and a plan for implementation.\n##### (d) Form\nThe report required by subsection (c) shall be submitted in unclassified form, but may include a classified annex.\n##### (e) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Armed Services and the Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Armed Services and the Committee on Foreign Affairs of the House of Representatives.",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2424rs.xml",
      "text": "II\nCalendar No. 238\n119th CONGRESS\n1st Session\nS. 2424\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Ricketts (for himself, Mr. Bennet , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require a report of, and a strategy to combat, arms sales of the Government of the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tracking Hostile Industry Networks and Kit while Thwarting Weapons Imports from Chinese Entities Act of 2025 or the THINK TWICE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe People's Republic of China is the fourth largest arms exporter behind the United States, the Russian Federation, and France.\n**(2)**\nArms sales by entities in the People's Republic of China are an important element of the country's growing military power and geopolitical influence.\n**(3)**\nThe People's Republic of China uses arms sales to promote strategic interests, including\u2014\n**(A)**\nimproving the image and reputation of the People\u2019s Liberation Army;\n**(B)**\nacquiring performance data of Chinese-made weapons in contested environments, which can be utilized by the People's Liberation Army;\n**(C)**\nexacerbating tensions between the United States and traditional security partners;\n**(D)**\ngaining a foothold for further defense and security cooperation with certain countries;\n**(E)**\nbuilding relationships with senior political and military leaders in other countries, further expanding the diplomatic and strategic influence of the People\u2019s Republic of China;\n**(F)**\nprotecting economic interests of the People's Republic of China by ensuring the security of foreign partner governments to safeguard Chinese investments and Chinese workers;\n**(G)**\nexerting influence over the progression of conflicts to serve the broader geostrategic aims of the People's Republic of China;\n**(H)**\nimproving military operations and capabilities of partner states, thereby stabilizing regions of interest by addressing local issues, such as disturbances near the border of the People's Republic of China; and\n**(I)**\nsubsidizing the research and development and production costs of weapons systems of the People's Republic of China.\n#### 3. Report on arms sales of the People's Republic of China\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the Secretary of Defense, in coordination with the Secretary of State, shall submit to the appropriate congressional committees a report on arms sales facilitated by entities in the People\u2019s Republic of China.\n##### (b) Contents\nThe report required by subsection (a) shall include an analysis of\u2014\n**(1)**\nthe weapons systems and defense equipment originating from the People's Republic of China available for purchase;\n**(2)**\nthe technical aspects and capabilities of such weapons systems and defense equipment;\n**(3)**\nhow such weapons systems and defense equipment may impact the balance of power in the area of responsibility of each United States Combatant Command, when applicable;\n**(4)**\nthe weapons systems and defense equipment originating from the People's Republic of China that are considered direct alternatives to weapons systems and defense equipment originating from the United States;\n**(5)**\nthe weapons systems and defense equipment originating from the People\u2019s Republic of China that present the greatest security risks regarding the potential to collect intelligence on or compromise assets, weapons, or platforms of the United States;\n**(6)**\nthe countries mostly likely to procure weapons systems and defense equipment originating from the People's Republic of China, including the specific type, quantity, and estimated value in United States dollars of weapons, during the 1-year period following the date of the submission of the report;\n**(7)**\nthe weapons systems and defense equipment in development as of the date of the submission of the report by entities in the People's Republic of China that could be available on the global market not later than 5 years after such date;\n**(8)**\nthe factors that incentivize countries to procure such weapons systems and defense equipment, including costs, flexible payment conditions and financing, a lack of end-user agreements, and speed of sale and delivery; and\n**(9)**\nthe strategy of the People's Republic of China regarding arms sales and variables that could influence such strategy.\n##### (c) Form\n**(1) In general**\nThe report required by subsection (a) shall be submitted in unclassified form, but shall include a classified annex.\n**(2) Classified annex**\nThe classified annex required by paragraph (1) shall contain\u2014\n**(A)**\nan assessment by the National Intelligence Council of the contents required by subsection (b); and\n**(B)**\nan assessment by the Director of National Intelligence of the counterintelligence risks and risks of onward proliferation of technology and defense systems originating in the United States and created through the purchase, deployment, and use of weapons systems and defense equipment originating from the People\u2019s Republic of China by United States allies and partners.\n##### (d) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Armed Services, the Committee on Foreign Relations, and the Select Committee on Intelligence of the Senate; and\n**(2)**\nthe Committee on Armed Services, the Committee on Foreign Affairs, and the Permanent Select Committee on Intelligence of the House of Representatives.\n#### 4. Strategy to combat arms sales of the People's Republic of China\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Defense, shall develop a strategy to dissuade purchases of new weapons systems and defense equipment, excluding spare parts or parts for maintenance of previously procured weapons, originating from the People's Republic of China.\n##### (b) Elements\nThe strategy shall include the following elements:\n**(1)**\nAn information campaign targeting countries interested in procuring weapons systems and defense equipment originating from the People's Republic of China to warn such countries about\u2014\n**(A)**\npotential risks, including the lack of a proven track record in combat, insufficient training on the operation of the weapon or weapons system, reliability issues, and the lack of maintenance and spare parts available;\n**(B)**\nthe inability to integrate such weapons systems and defense equipment with weapons systems and defense equipment from the United States; and\n**(C)**\nthe potential limitation of future security cooperation with the United States that could arise if such weapons are acquired.\n**(2)**\nA description of actions the United States can take, including reforms to the foreign military sales, direct commercial sales, and foreign military financing processes, to make weapons systems and defense equipment from the United States more attractive to prospective buyers of weapons systems or defense equipment originating from the People's Republic of China.\n**(3)**\nA description of actions defense firms of the United States can take to provide competitive alternatives to prospective buyers of weapons systems and defense equipment originating from the People's Republic of China.\n**(4)**\nAn analysis of whether the use of sanctions, export controls, or other economic restrictions targeting buyers of new weapons systems or defense equipment originating from the People\u2019s Republic of China could serve as an effective deterrent.\n**(5)**\nA plan to ensure sufficient representation of defense firms of the United States, or trusted allies, at defense expositions where defense firms of the People\u2019s Republic of China are also attending.\n**(6)**\nA plan to combat Chinese disinformation campaigns targeting the performance of weapons or platforms produced by the United States or trusted allies.\n**(7)**\nA plan to ensure close coordination with Congress to prevent disjointed engagement with countries.\n##### (c) Report and implementation plan\nNot later than the date on which the strategy required by subsection (a) is completed, the Secretary of State shall submit to the appropriate congressional committees a report detailing the strategy and a plan for implementation.\n##### (d) Form\nThe report required by subsection (c) shall be submitted in unclassified form, but may include a classified annex.\n##### (e) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Armed Services and the Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Armed Services and the Committee on Foreign Affairs of the House of Representatives.",
      "versionDate": "2025-10-30",
      "versionType": "Reported in Senate"
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
            "name": "Arms control and nonproliferation",
            "updateDate": "2026-01-20T19:51:57Z"
          },
          {
            "name": "Asia",
            "updateDate": "2026-01-20T19:51:51Z"
          },
          {
            "name": "China",
            "updateDate": "2026-01-20T19:51:45Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-20T19:52:03Z"
          },
          {
            "name": "Military assistance, sales, and agreements",
            "updateDate": "2026-01-20T19:51:40Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-01-20T19:52:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-09-18T20:01:40Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2424is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2424rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "THINK TWICE Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:38:13Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Tracking Hostile Industry Networks and Kit while Thwarting Weapons Imports from Chinese Entities Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:38:13Z"
    },
    {
      "title": "THINK TWICE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "THINK TWICE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tracking Hostile Industry Networks and Kit while Thwarting Weapons Imports from Chinese Entities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a report of, and a strategy to combat, arms sales of the Government of the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:31Z"
    }
  ]
}
```
