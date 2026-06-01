# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1216?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1216
- Title: Taiwan Allies Fund Act
- Congress: 119
- Bill type: S
- Bill number: 1216
- Origin chamber: Senate
- Introduced date: 2025-03-31
- Update date: 2026-03-10T13:49:20Z
- Update date including text: 2026-03-10T13:49:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in Senate
- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 321.
- Latest action: 2025-03-31: Introduced in Senate

## Actions

- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 321.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1216",
    "number": "1216",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Taiwan Allies Fund Act",
    "type": "S",
    "updateDate": "2026-03-10T13:49:20Z",
    "updateDateIncludingText": "2026-03-10T13:49:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 321.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-01-29",
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
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
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
            "date": "2026-02-10T16:28:24Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-29T14:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-01T00:57:13Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "UT"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NJ"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1216is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1216\nIN THE SENATE OF THE UNITED STATES\nMarch 31, 2025 Mr. Van Hollen (for himself, Mr. Curtis , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo support Taiwan's international space, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taiwan Allies Fund Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nTaiwan is a free and prosperous democracy of more than 23,000,000 people and an important contributor to peace and stability around the world.\n**(2)**\nThe People\u2019s Republic of China has engaged in a years-long campaign to diplomatically isolate Taiwan on the world stage.\n**(3)**\nSince 2013, the Gambia, S\u00e3o Tom\u00e9 and Pr\u00edncipe, Panama, the Dominican Republic, Burkina Faso, El Salvador, the Solomon Islands, Kiribati, Nicaragua, Honduras, and, most recently in 2024, Nauru have severed diplomatic relations with Taiwan in favor of diplomatic relations with the People\u2019s Republic of China.\n**(4)**\nThe People\u2019s Republic of China has used economic and diplomatic intimidation against countries pursuing unofficial relations with Taiwan, including Lithuania, Czechia, and the United States.\n**(5)**\nThe Taiwan Relations Act of 1979 ( Public Law 96\u20138 ) states that it is the policy of the United States to maintain the capacity of the United States to resist any resort to force or other forms of coercion that would jeopardize the security, or the social or economic system, of the people on Taiwan .\n**(6)**\nThe Taiwan Allies International Protection and Enhancement Initiative (TAIPEI) Act of 2019 ( Public Law 116\u2013135 ) states that the United States Government should\u2014\n**(A)**\nsupport Taiwan in strengthening its official diplomatic relationships as well as other partnerships with countries in the Indo-Pacific region and around the world ; and\n**(B)**\nconsider, in certain cases as appropriate and in alignment with United States interests, increasing its economic, security, and diplomatic engagement with nations that have demonstrably strengthened, enhanced, or upgraded relations with Taiwan .\n#### 3. Sense of Congress\nIt is the sense of Congress that the United States Government should\u2014\n**(1)**\nadvocate, as appropriate, for Taiwan\u2019s presence on the global stage, including at international organizations;\n**(2)**\npromote the preservation and expansion of Taiwan\u2019s official diplomatic relations with countries around the world;\n**(3)**\nexpand Taiwan\u2019s unofficial relations with countries around the world;\n**(4)**\nencourage countries with unofficial relations with Taiwan to deepen their engagement; and\n**(5)**\nadvance the economic development of countries that support democratic partners like Taiwan.\n#### 4. Taiwan Allies Fund\n##### (a) Authorization of appropriations\nOf the amounts made available under the Countering PRC Influence Fund for each of the fiscal years 2026, 2027, and 2028, there is authorized to be appropriated $40,000,000 for each such fiscal year to support Taiwan\u2019s international space.\n##### (b) Eligible countries\nAmounts available pursuant to the authorization of appropriations under subsection (a) may be used in countries that\u2014\n**(1)**\nmaintain official relations with Taiwan or have meaningfully strengthened unofficial relations with Taiwan;\n**(2)**\nhave been subject to coercion or pressure by the People\u2019s Republic of China due to their relations with Taiwan; and\n**(3)**\nlack the economic or political capability to effectively respond to such coercion or pressure by the People\u2019s Republic of China without the support of the United States.\n##### (c) Use of funds\nAmounts available pursuant to the authorization of appropriations under subsection (a) may be used to support any of the following activities in the countries described in subsection (b):\n**(1)**\nTo support health initiatives that provide alternatives to the Health Silk Road.\n**(2)**\nTo build the capacity and resilience of civil society, media, and other nongovernmental organizations in countering the influence and propaganda of the People\u2019s Republic of China.\n**(3)**\nTo diversify supply chains away from the People\u2019s Republic of China.\n**(4)**\nTo provide alternatives to People\u2019s Republic of China development assistance and project financing.\n**(5)**\nTo advance Taiwan\u2019s meaningful participation in international fora and multilateral organizations.\n**(6)**\nTo work with the private sector to provide United States or allied alternatives to People\u2019s Republic of China information and communications technology infrastructure and components.\n##### (d) Limitation on funds\nA country described in subsection (b) may not receive more than $5,000,000 of funds made available pursuant to the authorization of appropriations under subsection (a) during any fiscal year.\n##### (e) Implementation\n**(1) In general**\nThe Secretary of State, in consultation with the Administrator for the United States Agency for International Development, the Director of the American Institute in Taiwan, and the heads other relevant Federal agencies, shall coordinate and carry out activities described in subsection (c).\n**(2) Authorities**\nAmounts available pursuant to the authorization of appropriations under subsection (a) may be considered foreign assistance under the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) for purposes of making available the administrative authorities in that Act and may be transferred to, and merged with, funds made available for any provision of the Foreign Assistance Act of 1961 to carry out the purposes of this section, except that such funds shall remain available until expended.\n**(3) Coordination with Taiwan**\nIn order to maximize cost efficiency and eliminate duplication, the Secretary of State, in consultation with the Administrator for the United States Agency for International Development, should work with the Director of the American Institute in Taiwan to ensure coordination with relevant parties of Taiwan, as appropriate.\n**(4) Cost-sharing with Taiwan**\nThe Secretary of State should convey to relevant parties of Taiwan, as appropriate, that Taiwan should contribute commensurate assistance to countries described in subsection (b).\n**(5) Report**\n**(A) In general**\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter for two years, the Secretary of State shall submit to the appropriate congressional committees a report on activities described in this section that were carried out during the preceding fiscal year.\n**(B) Elements**\nEach report required by subparagraph (A) shall include\u2014\n**(i)**\nwith respect to each activity described in subsection (c)\u2014\n**(I)**\nthe amount of funding for the activity;\n**(II)**\nthe goal to which the activity relates; and\n**(III)**\nan assessment of the success of the activity to meet the goal to which the activity relates; and\n**(ii)**\nwith respect to this subsection\u2014\n**(I)**\nthe amount of funding for the activity provided by Taiwan during the preceding year, if any; and\n**(II)**\nan assessment of whether the funding described in subclause (I) is commensurate with funding provided by the United States.\n##### (f) Rule of construction\nNothing in this section may be construed to apply to or limit United States foreign assistance not provided using amounts available pursuant to the authorization of appropriations under subsection (a).\n##### (g) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Foreign Affairs of the House of Representatives.",
      "versionDate": "2025-03-31",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1216rs.xml",
      "text": "II\nCalendar No. 321\n119th CONGRESS\n2d Session\nS. 1216\nIN THE SENATE OF THE UNITED STATES\nMarch 31, 2025 Mr. Van Hollen (for himself, Mr. Curtis , Mr. Kim , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nFebruary 10, 2026 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo support Taiwan's international space, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taiwan Allies Fund Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nTaiwan is a free and prosperous democracy of more than 23,000,000 people and an important contributor to peace and stability around the world.\n**(2)**\nThe People\u2019s Republic of China has engaged in a years-long campaign to diplomatically isolate Taiwan on the world stage.\n**(3)**\nSince 2013, the Gambia, S\u00e3o Tom\u00e9 and Pr\u00edncipe, Panama, the Dominican Republic, Burkina Faso, El Salvador, the Solomon Islands, Kiribati, Nicaragua, Honduras, and, most recently in 2024, Nauru have severed diplomatic relations with Taiwan in favor of diplomatic relations with the People\u2019s Republic of China.\n**(4)**\nThe People\u2019s Republic of China has used economic and diplomatic intimidation against countries pursuing unofficial relations with Taiwan, including Lithuania, Czechia, and the United States.\n**(5)**\nThe Taiwan Relations Act of 1979 ( Public Law 96\u20138 ) states that it is the policy of the United States to maintain the capacity of the United States to resist any resort to force or other forms of coercion that would jeopardize the security, or the social or economic system, of the people on Taiwan .\n**(6)**\nThe Taiwan Allies International Protection and Enhancement Initiative (TAIPEI) Act of 2019 ( Public Law 116\u2013135 ) states that the United States Government should\u2014\n**(A)**\nsupport Taiwan in strengthening its official diplomatic relationships as well as other partnerships with countries in the Indo-Pacific region and around the world ; and\n**(B)**\nconsider, in certain cases as appropriate and in alignment with United States interests, increasing its economic, security, and diplomatic engagement with nations that have demonstrably strengthened, enhanced, or upgraded relations with Taiwan .\n#### 3. Sense of Congress\nIt is the sense of Congress that the United States Government should\u2014\n**(1)**\nadvocate, as appropriate, for Taiwan\u2019s presence on the global stage, including at international organizations;\n**(2)**\npromote the preservation and expansion of Taiwan\u2019s official diplomatic relations with countries around the world;\n**(3)**\nexpand Taiwan\u2019s unofficial relations with countries around the world;\n**(4)**\nencourage countries with unofficial relations with Taiwan to deepen their engagement; and\n**(5)**\nadvance the economic development of countries that support democratic partners like Taiwan.\n#### 4. Taiwan Allies Fund\n##### (a) Authorization of appropriations\nOf the amounts made available under the Countering PRC Influence Fund for each of the fiscal years 2026, 2027, and 2028, there is authorized to be appropriated $40,000,000 for each such fiscal year to support Taiwan\u2019s international space.\n##### (b) Eligible countries\nAmounts available pursuant to the authorization of appropriations under subsection (a) may be used in countries that\u2014\n**(1)**\nmaintain official relations with Taiwan or have meaningfully strengthened unofficial relations with Taiwan;\n**(2)**\nhave been subject to coercion or pressure by the People\u2019s Republic of China due to their relations with Taiwan; and\n**(3)**\nlack the economic or political capability to effectively respond to such coercion or pressure by the People\u2019s Republic of China without the support of the United States.\n##### (c) Use of funds\nAmounts available pursuant to the authorization of appropriations under subsection (a) may be used to support any of the following activities in the countries described in subsection (b):\n**(1)**\nTo support health initiatives that provide alternatives to the Health Silk Road.\n**(2)**\nTo build the capacity and resilience of civil society, media, and other nongovernmental organizations in countering the influence and propaganda of the People\u2019s Republic of China.\n**(3)**\nTo diversify supply chains away from the People\u2019s Republic of China.\n**(4)**\nTo provide alternatives to People\u2019s Republic of China development assistance and project financing.\n**(5)**\nTo advance Taiwan\u2019s meaningful participation in international fora and multilateral organizations.\n**(6)**\nTo work with the private sector to provide United States or allied alternatives to People\u2019s Republic of China information and communications technology infrastructure and components.\n##### (d) Limitation on funds\nA country described in subsection (b) may not receive more than $5,000,000 of funds made available pursuant to the authorization of appropriations under subsection (a) during any fiscal year.\n##### (e) Implementation\n**(1) In general**\nThe Secretary of State, in consultation with the Administrator for the United States Agency for International Development, the Director of the American Institute in Taiwan, and the heads other relevant Federal agencies, shall coordinate and carry out activities described in subsection (c).\n**(2) Authorities**\nAmounts available pursuant to the authorization of appropriations under subsection (a) may be considered foreign assistance under the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) for purposes of making available the administrative authorities in that Act and may be transferred to, and merged with, funds made available for any provision of the Foreign Assistance Act of 1961 to carry out the purposes of this section, except that such funds shall remain available until expended.\n**(3) Coordination with Taiwan**\nIn order to maximize cost efficiency and eliminate duplication, the Secretary of State, in consultation with the Administrator for the United States Agency for International Development, should work with the Director of the American Institute in Taiwan to ensure coordination with relevant parties of Taiwan, as appropriate.\n**(4) Cost-sharing with Taiwan**\nThe Secretary of State should convey to relevant parties of Taiwan, as appropriate, that Taiwan should contribute commensurate assistance to countries described in subsection (b).\n**(5) Report**\n**(A) In general**\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter for two years, the Secretary of State shall submit to the appropriate congressional committees a report on activities described in this section that were carried out during the preceding fiscal year.\n**(B) Elements**\nEach report required by subparagraph (A) shall include\u2014\n**(i)**\nwith respect to each activity described in subsection (c)\u2014\n**(I)**\nthe amount of funding for the activity;\n**(II)**\nthe goal to which the activity relates; and\n**(III)**\nan assessment of the success of the activity to meet the goal to which the activity relates; and\n**(ii)**\nwith respect to this subsection\u2014\n**(I)**\nthe amount of funding for the activity provided by Taiwan during the preceding year, if any; and\n**(II)**\nan assessment of whether the funding described in subclause (I) is commensurate with funding provided by the United States.\n##### (f) Rule of construction\nNothing in this section may be construed to apply to or limit United States foreign assistance not provided using amounts available pursuant to the authorization of appropriations under subsection (a).\n##### (g) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Foreign Affairs of the House of Representatives.",
      "versionDate": "2026-02-10",
      "versionType": "Reported in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "2559",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Taiwan Allies Fund Act",
      "type": "HR"
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
            "updateDate": "2026-03-10T13:48:34Z"
          },
          {
            "name": "China",
            "updateDate": "2026-03-10T13:48:27Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-10T13:49:19Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2026-03-10T13:48:57Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-03-10T13:49:12Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2026-03-10T13:48:48Z"
          },
          {
            "name": "Taiwan",
            "updateDate": "2026-03-10T13:48:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-14T14:57:27Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1216is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1216rs.xml"
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
      "title": "Taiwan Allies Fund Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-12T04:38:20Z"
    },
    {
      "title": "Taiwan Allies Fund Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Taiwan Allies Fund Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to support Taiwan's international space, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:20Z"
    }
  ]
}
```
