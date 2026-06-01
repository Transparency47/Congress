# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2978?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2978
- Title: Designating the Russian Federation as a State Sponsor of Terrorism Act
- Congress: 119
- Bill type: S
- Bill number: 2978
- Origin chamber: Senate
- Introduced date: 2025-10-07
- Update date: 2026-04-15T14:09:15Z
- Update date including text: 2026-04-15T14:09:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-07: Introduced in Senate
- 2025-10-07 - IntroReferral: Introduced in Senate
- 2025-10-07 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 246.
- Latest action: 2025-10-07: Introduced in Senate

## Actions

- 2025-10-07 - IntroReferral: Introduced in Senate
- 2025-10-07 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 246.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-07",
    "latestAction": {
      "actionDate": "2025-10-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2978",
    "number": "2978",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Designating the Russian Federation as a State Sponsor of Terrorism Act",
    "type": "S",
    "updateDate": "2026-04-15T14:09:15Z",
    "updateDateIncludingText": "2026-04-15T14:09:15Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 246.",
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
      "actionDate": "2025-10-07",
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
      "actionDate": "2025-10-07",
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
            "date": "2025-10-30T15:44:11Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:03:59Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-07T18:29:13Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "CT"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "AL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2978is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2978\nIN THE SENATE OF THE UNITED STATES\nOctober 7, 2025 Mr. Graham (for himself, Mr. Blumenthal , Mrs. Britt , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo provide for the designation of the Russian Federation as a state sponsor of terrorism.\n#### 1. Short title\nThis Act may be cited as the Designating the Russian Federation as a State Sponsor of Terrorism Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Russian Federation's aggression in Ukraine has targeted innocent civilians, including children.\n**(2)**\nThe Government of Ukraine estimates that at least 648 Ukrainian children have been killed and at least 2,047 Ukrainian children have been wounded since the start of President Vladimir Putin\u2019s invasion of Ukraine in February 2022.\n**(3)**\nThe Government of Ukraine estimates that the Russian Federation has kidnapped, deported, or displaced at least 19,546 Ukrainian children to the Russian Federation, Russian-occupied territories, and other locations since the invasion of Ukraine in February 2022 and continues to practice such illegal and inhumane actions.\n**(4)**\nThe Russian Federation has kidnapped, deported, or displaced Ukrainian children as young as a few months to 17 years of age according to reliable reports.\n**(5)**\nPresident Putin\u2019s regime seeks the Russification of Ukrainian children through kidnapping, deportation, or displacement to destroy their Ukrainian identity.\n**(6)**\nMany of these Ukrainian children are forced into re-education camps or youth paramilitary organizations in the Russian Federation and other locations, with the intent of training them for future deployment as service members in the Russian Armed Forces.\n**(7)**\nIn November 2024, the United Kingdom stated that the Government of the Russian Federation seeks to accomplish Russification by expos[ing] Ukrainian children to a curriculum that rewrites Russian and Ukrainian history, glorifies Russian military actions, promotes allegiance to Russia, and in some cases involves military training .\n**(8)**\nUkraine has made efforts to repatriate these kidnapped and deported children, including during the peace talks that occurred in Istanbul, Turkey in June 2025, where Ukraine presented the Russian delegation with a list of 339 names of kidnapped children to return home.\n**(9)**\nIn response to the proposal put forth by Ukraine in Istanbul, Turkey, the Russian delegation, led by Vladimir Medinsky, stated that these children were rescued by Russian soldiers and dismissed the request.\n**(10)**\nUnited States law authorizes the designation of countries as state sponsors of terrorism if they have repeatedly provided support for acts of international terrorism.\n**(11)**\nSection 2331(1) of title 18, United States Code, defines international terrorism as activities that\u2014\n(A) involve violent acts or acts dangerous to human life that are a violation of the criminal laws of the United States or of any State, or that would be a criminal violation if committed within the jurisdiction of the United States or of any State; (B) appear to be intended\u2014 (i) to intimidate or coerce a civilian population; (ii) to influence the policy of a government by intimidation or coercion; or (iii) to affect the conduct of a government by mass destruction, assassination, or kidnapping; and (C) occur primarily outside the territorial jurisdiction of the United States, or transcend national boundaries in terms of the means by which they are accomplished, the persons they appear intended to intimidate or coerce, or the locale in which their perpetrators operate or seek asylum; .\n**(12)**\nAt the direction of President Putin, the Government of the Russian Federation has promoted, and continues to promote, these acts of international terrorism, including the kidnapping of Ukrainian children, which would constitute a criminal violation if committed within the jurisdiction of the United States.\n**(13)**\nDuring the 117th Congress, the Senate unanimously adopted\u2014\n**(A)**\nSenate Resolution 623, which called for the Secretary of State to designate the Russian Federation as a state sponsor of terrorism; and\n**(B)**\nSenate Resolution 546, which condemned the actions of the Russian Federation, President Putin, members of the Russian Security Council, the Russian Armed Forces, and Russian military commanders for committing atrocities and alleged war crimes against the people of Ukraine.\n**(14)**\nThe United States continues to have a range of tools available to hold the Russian Federation accountable for these egregious actions.\n#### 3. Designation of the Russian Federation as a state sponsor of terrorism\n##### (a) Certification\nNot later than 60 days after the effective date of this Act, the Secretary of State shall submit a report to Congress that certifies whether\u2014\n**(1)**\nthe Ukrainian children who were kidnapped, deported, or forcibly removed from Ukrainian territory or temporarily occupied Ukrainian territory since the Russian Federation's invasion of Ukraine in February 2022 have been reunited with their families or guardians in a secure environment; and\n**(2)**\nthe process of full reintegration of such children into Ukrainian society is underway.\n##### (b) Designation\nIf the Secretary of State cannot certify the actions described in paragraphs (1) and (2) of subsections (a) have occurred, the Secretary shall immediately designate the Russian Federation as a state sponsor of terrorism pursuant to\u2014\n**(1)**\nsection 1754(c) of the National Defense Authorization Act for Fiscal Year 2019 ( 50 U.S.C. 4813(c) );\n**(2)**\nsection 40 of the Arms Export Control Act ( 22 U.S.C. 2780 );\n**(3)**\nsection 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 ); and\n**(4)**\nany other relevant provision of law.\n#### 4. Rescission of the designation of the Russian Federation as a state sponsor of terrorism\nThe Secretary of State may rescind the designation required under section 3(b) on or after the date that is 45 days after the date on which the Secretary certifies to Congress, pursuant to the provision of law under which such designation was made, that\u2014\n**(1)**\nthe Government of the Russian Federation\u2014\n**(A)**\nhas not provided support for international terrorism during the preceding 3-month period; and\n**(B)**\nhas provided assurances that such government will not support acts of international terrorism in the future;\n**(2)**\nall of the children kidnapped, deported, or forcibly transferred from Ukrainian territory or temporarily occupied Ukrainian territory since the Russian Federation\u2019s invasion of Ukraine in February 2022 have been reunited with their families and guardians in a secure environment; and\n**(3)**\nthe process of full reintegration of such children into Ukrainian society is underway.\n#### 5. Effective date\nThis Act shall take effect on the date that is 1 day after the date of the enactment of this Act.",
      "versionDate": "2025-10-07",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2978rs.xml",
      "text": "II\nCalendar No. 246\n119th CONGRESS\n1st Session\nS. 2978\nIN THE SENATE OF THE UNITED STATES\nOctober 7, 2025 Mr. Graham (for himself, Mr. Blumenthal , Mrs. Britt , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo provide for the designation of the Russian Federation as a state sponsor of terrorism.\n#### 1. Short title\nThis Act may be cited as the Designating the Russian Federation as a State Sponsor of Terrorism Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Russian Federation's aggression in Ukraine has targeted innocent civilians, including children.\n**(2)**\nThe Government of Ukraine estimates that at least 648 Ukrainian children have been killed and at least 2,047 Ukrainian children have been wounded since the start of President Vladimir Putin\u2019s invasion of Ukraine in February 2022.\n**(3)**\nThe Government of Ukraine estimates that the Russian Federation has kidnapped, deported, or displaced at least 19,546 Ukrainian children to the Russian Federation, Russian-occupied territories, and other locations since the invasion of Ukraine in February 2022 and continues to practice such illegal and inhumane actions.\n**(4)**\nThe Russian Federation has kidnapped, deported, or displaced Ukrainian children as young as a few months to 17 years of age according to reliable reports.\n**(5)**\nPresident Putin\u2019s regime seeks the Russification of Ukrainian children through kidnapping, deportation, or displacement to destroy their Ukrainian identity.\n**(6)**\nMany of these Ukrainian children are forced into re-education camps or youth paramilitary organizations in the Russian Federation and other locations, with the intent of training them for future deployment as service members in the Russian Armed Forces.\n**(7)**\nIn November 2024, the United Kingdom stated that the Government of the Russian Federation seeks to accomplish Russification by expos[ing] Ukrainian children to a curriculum that rewrites Russian and Ukrainian history, glorifies Russian military actions, promotes allegiance to Russia, and in some cases involves military training .\n**(8)**\nUkraine has made efforts to repatriate these kidnapped and deported children, including during the peace talks that occurred in Istanbul, Turkey in June 2025, where Ukraine presented the Russian delegation with a list of 339 names of kidnapped children to return home.\n**(9)**\nIn response to the proposal put forth by Ukraine in Istanbul, Turkey, the Russian delegation, led by Vladimir Medinsky, stated that these children were rescued by Russian soldiers and dismissed the request.\n**(10)**\nUnited States law authorizes the designation of countries as state sponsors of terrorism if they have repeatedly provided support for acts of international terrorism.\n**(11)**\nSection 2331(1) of title 18, United States Code, defines international terrorism as activities that\u2014\n(A) involve violent acts or acts dangerous to human life that are a violation of the criminal laws of the United States or of any State, or that would be a criminal violation if committed within the jurisdiction of the United States or of any State; (B) appear to be intended\u2014 (i) to intimidate or coerce a civilian population; (ii) to influence the policy of a government by intimidation or coercion; or (iii) to affect the conduct of a government by mass destruction, assassination, or kidnapping; and (C) occur primarily outside the territorial jurisdiction of the United States, or transcend national boundaries in terms of the means by which they are accomplished, the persons they appear intended to intimidate or coerce, or the locale in which their perpetrators operate or seek asylum; .\n**(12)**\nAt the direction of President Putin, the Government of the Russian Federation has promoted, and continues to promote, these acts of international terrorism, including the kidnapping of Ukrainian children, which would constitute a criminal violation if committed within the jurisdiction of the United States.\n**(13)**\nDuring the 117th Congress, the Senate unanimously adopted\u2014\n**(A)**\nSenate Resolution 623, which called for the Secretary of State to designate the Russian Federation as a state sponsor of terrorism; and\n**(B)**\nSenate Resolution 546, which condemned the actions of the Russian Federation, President Putin, members of the Russian Security Council, the Russian Armed Forces, and Russian military commanders for committing atrocities and alleged war crimes against the people of Ukraine.\n**(14)**\nThe United States continues to have a range of tools available to hold the Russian Federation accountable for these egregious actions.\n#### 3. Designation of the Russian Federation as a state sponsor of terrorism\n##### (a) Certification\nNot later than 60 days after the effective date of this Act, the Secretary of State shall submit a report to Congress that certifies whether\u2014\n**(1)**\nthe Ukrainian children who were kidnapped, deported, or forcibly removed from Ukrainian territory or temporarily occupied Ukrainian territory since the Russian Federation's invasion of Ukraine in February 2022 have been reunited with their families or guardians in a secure environment; and\n**(2)**\nthe process of full reintegration of such children into Ukrainian society is underway.\n##### (b) Designation\nIf the Secretary of State cannot certify the actions described in paragraphs (1) and (2) of subsections (a) have occurred, the Secretary shall immediately designate the Russian Federation as a state sponsor of terrorism pursuant to\u2014\n**(1)**\nsection 1754(c) of the National Defense Authorization Act for Fiscal Year 2019 ( 50 U.S.C. 4813(c) );\n**(2)**\nsection 40 of the Arms Export Control Act ( 22 U.S.C. 2780 );\n**(3)**\nsection 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 ); and\n**(4)**\nany other relevant provision of law.\n#### 4. Rescission of the designation of the Russian Federation as a state sponsor of terrorism\nThe Secretary of State may rescind the designation required under section 3(b) on or after the date that is 45 days after the date on which the Secretary certifies to Congress, pursuant to the provision of law under which such designation was made, that\u2014\n**(1)**\nthe Government of the Russian Federation\u2014\n**(A)**\nhas not provided support for international terrorism during the preceding 3-month period; and\n**(B)**\nhas provided assurances that such government will not support acts of international terrorism in the future;\n**(2)**\nall of the children kidnapped, deported, or forcibly transferred from Ukrainian territory or temporarily occupied Ukrainian territory since the Russian Federation\u2019s invasion of Ukraine in February 2022 have been reunited with their families and guardians in a secure environment; and\n**(3)**\nthe process of full reintegration of such children into Ukrainian society is underway.\n#### 5. Effective date\nThis Act shall take effect on the date that is 1 day after the date of the enactment of this Act.",
      "versionDate": "2025-10-30",
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
        "actionDate": "2025-09-16",
        "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 160."
      },
      "number": "2805",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Designating the Russian Federation as a State Sponsor of Terrorism Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-21",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "5797",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Designating the Russian Federation as a State Sponsor of Terrorism Act",
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
            "name": "Detention of persons",
            "updateDate": "2026-04-01T20:34:32Z"
          },
          {
            "name": "Europe",
            "updateDate": "2026-04-01T20:34:10Z"
          },
          {
            "name": "Russia",
            "updateDate": "2026-04-01T20:34:05Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2026-04-01T20:34:16Z"
          },
          {
            "name": "Ukraine",
            "updateDate": "2026-04-01T20:34:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-11-19T21:17:41Z"
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
      "date": "2025-10-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2978is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2978rs.xml"
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
      "title": "Designating the Russian Federation as a State Sponsor of Terrorism Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:53:13Z"
    },
    {
      "title": "Designating the Russian Federation as a State Sponsor of Terrorism Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Designating the Russian Federation as a State Sponsor of Terrorism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the designation of the Russian Federation as a state sponsor of terrorism.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:03:13Z"
    }
  ]
}
```
