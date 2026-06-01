# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2712?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2712
- Title: Reclaiming Congressional Trade Authority Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2712
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-05-14T15:15:17Z
- Update date including text: 2025-05-14T15:15:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-08 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-08 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2712",
    "number": "2712",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Reclaiming Congressional Trade Authority Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-14T15:15:17Z",
    "updateDateIncludingText": "2025-05-14T15:15:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-08T14:02:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2712ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2712\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo limit the authority of the President to modify duty rates for national security reasons and to limit the authority of the United States Trade Representative to impose certain duties or import restrictions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reclaiming Congressional Trade Authority Act of 2025 .\n#### 2. Limitation on authority of President to modify duty rates for national security reasons\n##### (a) Authority To modify duty rates for national security reasons\nNotwithstanding any other provision of law and except as provided in subsection (c), the President may proclaim a new or additional national security duty on an article imported into the United States only if\u2014\n**(1)**\nthe President, not later than 30 calendar days after making the national security determination that is the basis for the new or additional duty, submits to the International Trade Commission the duty proposal, including\u2014\n**(A)**\na description of each article for which the President recommends a new or additional duty;\n**(B)**\nthe proposed new or additional duty rate; and\n**(C)**\nthe proposed duration of that rate;\n**(2)**\nthe President, not later than 15 calendar days after submitting the duty proposal under paragraph (1), submits to Congress a request for authorization to modify duty rates in accordance with that duty proposal, including\u2014\n**(A)**\na report by the Secretary of Defense explaining why the proposal is in the interest of national security; and\n**(B)**\na report by the International Trade Commission assessing the likely impact of the proposal on the economy of the United States as a whole and specific industry sectors;\n**(3)**\nthe President consults with the Committee on Finance and the Committee on Armed Services of the Senate and the Committee on Ways and Means and the Committee on Armed Services of the House of Representatives regarding the duty proposal under paragraph (1), including\u2014\n**(A)**\nthe short-term and long-term goals of the proposal;\n**(B)**\nan action plan to achieve those goals; and\n**(C)**\nplans to consult with officials of countries impacted by the proposal to resolve any issues relating to the proposal; and\n**(4)**\na joint resolution of approval under subsection (b) is enacted.\n##### (b) Joint resolution of approval\n**(1) Joint resolution of approval defined**\nIn this subsection, the term joint resolution of approval means a joint resolution the sole matter after the resolving clause of which is as follows: That Congress authorizes the President to proclaim duty rates as set forth in the request of the President on ___________ , with the blank space being filled with the date of the request submitted under subsection (a)(2).\n**(2) Introduction**\nA joint resolution of approval may be introduced in either House of Congress by any Member during the 15-legislative day period beginning on the date on which the President submits to Congress the material set forth in subsection (a)(2).\n**(3) Expedited procedures**\nThe provisions of subsections (b) through (f) of section 152 of the Trade Act of 1974 ( 19 U.S.C. 2192 ) apply to a joint resolution of approval to the same extent that such subsections apply to joint resolutions under such section 152.\n**(4) Rules of House of Representatives and Senate**\nThis subsection is enacted by Congress\u2014\n**(A)**\nas an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House in the case of a joint resolution of approval, and supersedes other rules only to the extent that it is inconsistent with such rules; and\n**(B)**\nwith full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.\n##### (c) Exception for urgent action\nNotwithstanding the requirements of subsection (a), the President may proclaim a new or additional national security duty for one period of 120 calendar days if the President determines that urgent action is necessary\u2014\n**(1)**\nto address a national emergency;\n**(2)**\nfor the prevention or mitigation of, or to respond to, loss of life or property;\n**(3)**\nto address an imminent threat to health or safety;\n**(4)**\nfor the enforcement of criminal laws; or\n**(5)**\nfor national security.\n##### (d) National security duty defined\nIn this section, the term national security duty means the following:\n**(1)**\nA duty proclaimed pursuant to\u2014\n**(A)**\nsection 232 of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862 );\n**(B)**\nthe Trading with the Enemy Act ( 50 U.S.C. 4301 et seq. ); or\n**(C)**\nthe International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ).\n**(2)**\nA duty proclaimed pursuant to any other provision of law if in reports or other public statements regarding the duty the President or another cabinet-level official identifies national security as a significant reason for proclaiming the duty.\n#### 3. Conditions on use of authority by United States Trade Representative to impose duties or other import restrictions\n##### (a) In general\nSection 301(c) of the Trade Act of 1974 ( 19 U.S.C. 2411(c) ) is amended by adding at the end the following:\n(7) (A) The Trade Representative may take action pursuant to paragraph (1)(B) only if\u2014 (i) the Trade Representative submits to the International Trade Commission a proposal for duties or other import restrictions under that paragraph, including\u2014 (I) a description of each article covered by that proposal; (II) the proposed new or additional duty rate; and (III) the proposed duration of that rate; (ii) the Trade Representative submits to Congress a notification of intent to impose duties or import restrictions under that paragraph, including\u2014 (I) the proposal submitted under clause (i); and (II) a report by the International Trade Commission assessing the likely impact of the proposal on the economy of the United States as a whole and specific industry sectors; (iii) after submitting the notification under clause (ii), the Trade Representative consults with the Committee on Finance of the Senate and the Committee on Ways and Means of the House of Representatives and, if the proposal affects agricultural products, the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives; (iv) a period of 60 calendar days, beginning on the date on which the Trade Representative has completed consultations under clause (iii), has passed; and (v) no disapproval resolution under subparagraph (B) is passed during the period described in clause (iv). (B) (i) In this subparagraph, the term disapproval resolution means a joint resolution the sole matter after the resolving clause of which is as follows: That implementation of the proposal by the Trade Representative to impose duties or other import restrictions submitted to Congress on ________________ is not in the interest of the United States. , with the blank space being filled with the date on which the Trade Representative submitted to Congress the material described in subsection (A)(ii). (ii) Paragraph (2) of section 106(b) of the Bipartisan Congressional Trade Priorities and Accountability Act of 2015 ( 19 U.S.C. 4205(b) ) applies to a disapproval resolution under this subparagraph to the same extent that such paragraph applies to a procedural disapproval resolution under such section 106(b). .\n##### (b) Conforming amendment\nParagraph (1)(B) of such section is amended by inserting subject to paragraph (7), before impose duties .",
      "versionDate": "2025-04-08",
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
        "updateDate": "2025-05-14T15:15:17Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2712ih.xml"
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
      "title": "Reclaiming Congressional Trade Authority Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-17T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reclaiming Congressional Trade Authority Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the authority of the President to modify duty rates for national security reasons and to limit the authority of the United States Trade Representative to impose certain duties or import restrictions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T05:18:35Z"
    }
  ]
}
```
