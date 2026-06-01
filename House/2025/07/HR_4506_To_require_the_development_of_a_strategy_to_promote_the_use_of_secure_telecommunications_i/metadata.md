# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4506?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4506
- Title: Securing Global Telecommunications Act
- Congress: 119
- Bill type: HR
- Bill number: 4506
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-03-31T11:19:16Z
- Update date including text: 2026-03-31T11:19:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4506",
    "number": "4506",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000375",
        "district": "9",
        "firstName": "William",
        "fullName": "Rep. Keating, William R. [D-MA-9]",
        "lastName": "Keating",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Securing Global Telecommunications Act",
    "type": "HR",
    "updateDate": "2026-03-31T11:19:16Z",
    "updateDateIncludingText": "2026-03-31T11:19:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4506ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4506\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Keating (for himself and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the development of a strategy to promote the use of secure telecommunications infrastructure worldwide, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Global Telecommunications Act .\n#### 2. Sense of congress\nIt is the sense of Congress as follows:\n**(1)**\nThe United States Government should promote and take steps to ensure American leadership in strategic technology industries, including telecommunications infrastructure and other information and communications technologies.\n**(2)**\nThe expansive presence of companies linked to the Chinese Communist Party, such as Huawei, in global mobile networks and the national security implications thereof, such as the ability of the People\u2019s Republic of China to exfiltrate the information flowing through those networks and shut off countries\u2019 internet access, demonstrates the importance of the United States remaining at the technological frontier and the dire consequences of falling behind.\n**(3)**\nThe significant cost of countering Huawei\u2019s market leadership in telecommunications infrastructure around the world underscores the urgency of supporting the competitiveness of United States companies in next-generation information and communication technology.\n**(4)**\nTo remain a leader at the International Telecommunication Union (ITU) and preserve the ITU\u2019s technical integrity, the United States must work with emerging economies and developing nations to bolster global telecommunications security and protect American national security interests.\n**(5)**\nMultilateral cooperation with like-minded partners and allies is critical to carry out the significant effort of financing and promoting secure networks around the world and to achieve market leadership of trusted vendors in this sector.\n#### 3. Strategy for securing global telecommunications infrastructure\n##### (a) Strategy required\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall develop and submit to the Committees on Foreign Affairs of the House of Representatives and Energy and Commerce and the Committees on Foreign Relations and Commerce, Science, and Transportation and of the Senate a strategy, to be known as the Strategy to Secure Global Telecommunications Infrastructure (referred to in this Act as the Strategy ), to promote the use of secure telecommunication infrastructure in countries other than the United States.\n##### (b) Consultation required\nThe Secretary of State shall consult with the President of the Export-Import Bank of the United States, the Chief Executive Officer of the Development Finance Corporation, the Administrator of the United States Agency for International Development, the Director of the Trade and Development Agency, the Chair of the Federal Communications Commission, and the Assistant Secretary of Commerce for Communications and Information, in developing the Strategy, which shall consist of an approach led by the Department of State using the policy tools, and informed by the technical expertise, of the other Federal entities so consulted to achieve the goal described in subsection (a).\n##### (c) Elements\nThe Strategy shall also include sections on each of the following:\n**(1)**\nMobile networks, including a description of efforts by countries other than the United States to\u2014\n**(A)**\npromote trusted Open RAN technologies while protecting against any security risks posed by untrusted vendors in Open RAN networks;\n**(B)**\nuse financing mechanisms to assist rip-and-replace projects and to incentivize countries to choose trusted equipment vendors;\n**(C)**\nbolster multilateral cooperation, especially with developing countries and emerging economies, to promote the deployment of trusted wireless networks worldwide; and\n**(D)**\ncollaborate with trusted private sector companies to counter Chinese market leadership in the telecom equipment industry.\n**(2)**\nData centers, including a description of efforts to\u2014\n**(A)**\nutilize financing mechanisms to incentivize countries other than the United States to choose trusted data center providers; and\n**(B)**\nbolster multilateral cooperation, especially with developing countries and emerging economies, to promote the deployment of trusted data centers worldwide.\n**(3)**\nSixth (and future) generation technologies (6G), including a description of efforts to\u2014\n**(A)**\ndeepen cooperation with like-minded countries to promote United States and allied market leadership in 6G networks and technologies; and\n**(B)**\nincrease buy-in from developing countries and emerging countries on trusted technologies.\n**(4)**\nLow-Earth orbit satellites, aerostats, and stratospheric balloons, including a description of efforts to work with trusted private sector companies to retain the ability to quickly provide internet connection in response to emergency situations.\n#### 4. Report on malign influence at the international telecommunication union\n##### (a) Report\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall develop and submit to the Committees on Foreign Affairs and Energy and Commerce of the House of Representatives and the Committees on Foreign Relations and Commerce, Science, and Transportation the Senate a report on Russian and Chinese strategies and efforts\u2014\n**(1)**\nto expand the mandate of the International Telecommunication Union (ITU) to cover internet governance policy; and\n**(2)**\nto advance other actions favorable to authoritarian interests and/or hostile to fair, industry-led processes.\n##### (b) Elements\nThe report required by subsection (a) shall also identify efforts by China and Russia\u2014\n**(1)**\nto increase the ITU\u2019s jurisdiction over internet governance and to propose internet governance standards at the ITU;\n**(2)**\nto leverage their private sector actors to advance their national interests through the ITU, including\u2014\n**(A)**\nencouraging Chinese and Russian companies to leverage their market power to pressure other member countries to deliver favorable decisions on ITU elections; and\n**(B)**\nChina\u2019s efforts to leverage Huawei\u2019s role as the primary telecommunications equipment and services provider for many developing countries to compel such countries to deliver favorable decisions on standards proposals, election victories, candidate selection, and other levers of power at the ITU; and\n**(3)**\nto use the influence of Chinese and Russian nationals serving in the ITU to advantage the companies, standards decisions, and candidates that advance the CCP and Kremlin\u2019s interests.\n##### (c) Form\nThe report required by this section shall be submitted in unclassified form, but may include a classified annex.\n#### 5. Report on multilateral coordination\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State, in coordination with the President of the Export-Import Bank of the United States, the Administrator for the United States Agency on International Development, the Chief Executive Officer of the Development Finance Corporation, the Chair of the Federal Communications Commission, and the Assistant Secretary of Commerce for Communications and Information, shall develop and submit to the Committees on Foreign Affairs and Energy and Commerce and of the House of Representatives and the Committees Foreign Relations and on Commerce, Science, and Transportation and of the Senate a report that identifies opportunities for greater collaboration with allies and partners to promote secure information and communications technology infrastructure in countries other than the United States, including through\u2014\n**(1)**\njoint financing efforts to help trusted vendors win bids to build out information and communications technology (ICT) infrastructure;\n**(2)**\nincorporating ICT focuses into allies\u2019 and partners\u2019 international development finance initiatives; and\n**(3)**\ndiplomatic coordination to emphasize the importance of secure telecommunications infrastructure to countries using untrusted providers.",
      "versionDate": "2025-07-17",
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
        "name": "International Affairs",
        "updateDate": "2025-09-18T18:20:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-17",
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
          "measure-id": "id119hr4506",
          "measure-number": "4506",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-17",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4506v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Securing Global Telecommunications Act</strong></p><p>This bill requires the Department of State to develop and submit to Congress a strategy to promote the use of secure telecommunication infrastructure in countries other than the United States.</p><p>The State Department must also report to Congress on (1) efforts by China and Russia to advance authoritarian interests or oppose fair, industry-led processes at the International Telecommunication Union, the U.N. agency involved with setting telecommunications standards and related regulatory activities; and (2) opportunities for greater collaboration with allies and partners to promote secure information and communications technology infrastructure in countries other than the United States.</p>"
        },
        "title": "Securing Global Telecommunications Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4506.xml",
    "summary": {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing Global Telecommunications Act</strong></p><p>This bill requires the Department of State to develop and submit to Congress a strategy to promote the use of secure telecommunication infrastructure in countries other than the United States.</p><p>The State Department must also report to Congress on (1) efforts by China and Russia to advance authoritarian interests or oppose fair, industry-led processes at the International Telecommunication Union, the U.N. agency involved with setting telecommunications standards and related regulatory activities; and (2) opportunities for greater collaboration with allies and partners to promote secure information and communications technology infrastructure in countries other than the United States.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4506"
    },
    "title": "Securing Global Telecommunications Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing Global Telecommunications Act</strong></p><p>This bill requires the Department of State to develop and submit to Congress a strategy to promote the use of secure telecommunication infrastructure in countries other than the United States.</p><p>The State Department must also report to Congress on (1) efforts by China and Russia to advance authoritarian interests or oppose fair, industry-led processes at the International Telecommunication Union, the U.N. agency involved with setting telecommunications standards and related regulatory activities; and (2) opportunities for greater collaboration with allies and partners to promote secure information and communications technology infrastructure in countries other than the United States.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4506"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4506ih.xml"
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
      "title": "Securing Global Telecommunications Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Global Telecommunications Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the development of a strategy to promote the use of secure telecommunications infrastructure worldwide, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:57Z"
    }
  ]
}
```
