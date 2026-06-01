# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4335?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4335
- Title: Abraham Accords Defense Against Terror Act
- Congress: 119
- Bill type: HR
- Bill number: 4335
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-02-27T16:20:23Z
- Update date including text: 2026-02-27T16:20:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 31 - 19.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 31 - 19.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4335",
    "number": "4335",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Abraham Accords Defense Against Terror Act",
    "type": "HR",
    "updateDate": "2026-02-27T16:20:23Z",
    "updateDateIncludingText": "2026-02-27T16:20:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 31 - 19.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
        "item": [
          {
            "date": "2025-07-22T15:36:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-10T15:07:00Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "MT"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "WI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "PA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TN"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "MN"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "SC"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NE"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "GA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "WA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NJ"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "IA"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TN"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TN"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "CO"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "AZ"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "MN"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "IN"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "AR"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "NE"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "FL"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "PA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "KS"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4335ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4335\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Lawler (for himself, Mr. Moskowitz , Mr. Zinke , Mr. Davis of North Carolina , Mr. Steil , Mr. Fitzpatrick , Ms. Salazar , Mr. Kustoff , Mr. McCaul , Mr. Stauber , Mr. Wilson of South Carolina , Mr. Bacon , Mrs. Luna , Mr. Carter of Georgia , Mr. Baumgartner , Mr. Gottheimer , Mr. Nunn of Iowa , Mr. Rose , Mr. Fleischmann , Mr. Edwards , Mr. Crank , Mr. Hamadeh of Arizona , Ms. Stefanik , Mr. Garbarino , Mr. Finstad , and Mr. Messmer ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide authority to enhance security assistance with countries that are engaged in regional security cooperation efforts in the Middle East and North Africa, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Abraham Accords Defense Against Terror Act .\n#### 2. Authority to enhance security assistance with countries that are engaged in regional security cooperation efforts in the Middle East and North Africa\n##### (a) Statement of policy\nIt is the policy of the United States to work with allies and partners to safeguard freedom of navigation, protect critical infrastructure, uphold basic principles of international law, and protect United States citizens from threats posed by Iran and Iran-aligned entities in the Middle East and North Africa.\n##### (b) Authority\nThe Secretary of State shall\u2014\n**(1)**\nidentify countries that\u2014\n**(A)**\nhave normalized diplomatic relations with the State of Israel; and\n**(B)**\nare engaged in regional security cooperation efforts in the Middle East and North Africa to combat threats posed by Iran and Iran-aligned entities; and\n**(2)**\nin order to meet the policy described in subsection (a), provide approval for the sale or lease, a license or other approval for the export, or the transfer of defense articles or defense services to countries identified by the Secretary under paragraph (1) in accordance with the expedited approval provisions of subsection (c).\n##### (c) Expedited approval provisions\nIn the case of a sale or lease of defense articles or defense services under section 3, 21, or 36 of the Arms Export Control Act ( 22 U.S.C. 2753 , 2761, or 2776) to a country identified by the Secretary of State under subsection (b)(1), a license or other approval under section 38 of such Act ( 22 U.S.C. 2778 ) for the export of defense articles or defense services to such a country (or of a commercial agreement that involves the manufacture in such a country of any item of significant combat equipment on the United States Munitions List in accordance with section 36(d) of such Act ( 22 U.S.C. 2776(d) )), or a transfer of excess defense articles under section 516(c)(2) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2321j(c)(2) ) to such a country, the President shall\u2014\n**(1)**\nnotwithstanding the time limitations described in any of such sections, submit to Congress a certification described in such sections, at least 15 calendar days before sale, lease, license or other approval, or transfer of the defense articles or defense services is approved; and\n**(2)**\ninclude in the certification\u2014\n**(A)**\ninformation on why the provision of such defense articles or services is related to or in furtherance of the policy described in subsection (a); and\n**(B)**\na summary of steps taken by the United States Government to ensure that any sensitive United States technology, information, or capabilities that may be provided to such a country by reason of the provision of such defense articles or services are not acquired by\u2014\n**(i)**\nthe People\u2019s Republic of China or any entity owned or controlled by the People\u2019s Republic of China; or\n**(ii)**\nthe Russian Federation or any entity owned or controlled by the Russian Federation.\n##### (d) Strategy\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, and every 60 days thereafter, the Secretary of State shall submit to the appropriate congressional committees, in writing, a strategy on the implementation of this section.\n**(2) Matters to be included**\nThe strategy required by this subsection shall include the following:\n**(A)**\nAn overview of the security threats from Iran and Iran-aligned entities to both the United States and the countries identified by the Secretary of State under subsection (b)(1).\n**(B)**\nA description and assessment of the metrics and evaluation procedures used for implementing the policy described in subsection (a), including recommendations to improve multilateral cooperation between the United States and such countries and among such countries.\n**(C)**\nA description of the challenges to achieving full interoperability between the United States and such countries and the impact on progress to address the policy described in subsection (a), including efforts to address shared threats posed by Iran and Iran-aligned entities.\n**(D)**\nA description of measures to provide such countries interim capabilities until the cases described in clauses (i) and (ii) are delivered.\n**(E)**\nA description and assessment of\u2014\n**(i)**\nthe status of all pending sales of defense articles or defense services over $25,000,000, including Letters of Request and where applicable Letters of Offer and Acceptance, beginning 5 years prior to the date of the enactment of this Act, to such countries pursuant to the provisions of law specified in subsection (c);\n**(ii)**\na description of the delivery time-frames for all pending sales of defense articles or defense services over $25,000,000 to such countries pursuant to the provisions of law specified in subsection (c) and any measures that could be taken to expedite their delivery; and\n**(iii)**\nrecommendations to improve the process for authorizing the transfer of defense articles and services authorized under sections 36 and 38 of the Arms Export Control Act to such countries, including as it relates to delivery timeline.\n**(3) Form**\nThe report required by this subsection shall be submitted in unclassified form but may contain a classified annex.\n**(4) Definitions**\nIn this subsection\u2014\n**(A)**\nthe term appropriate congressional committees means\u2014\n**(i)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(ii)**\nthe Committee on Foreign Relations of the Senate; and\n**(B)**\nthe term Iran-aligned entity \u2014\n**(i)**\nincludes an entity that\u2014\n**(I)**\nis controlled or significantly influenced by the Government of Iran; and\n**(II)**\nknowingly receives material or financial support from the Government of Iran; and\n**(ii)**\nincludes\u2014\n**(I)**\nHezbollah;\n**(II)**\nthe Houthis; or\n**(III)**\nany other proxy group that furthers Iran\u2019s national security objectives.\n#### 3. Rule of construction\nNothing in this Act shall be construed as adversely affecting Israel\u2019s qualitative military edge, as defined in section 36(h)(3) of the Arms Export Control Act ( 22 U.S.C. 2776 ).",
      "versionDate": "2025-07-10",
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
            "name": "Africa",
            "updateDate": "2025-08-20T16:58:18Z"
          },
          {
            "name": "Arab-Israeli relations",
            "updateDate": "2025-08-20T16:57:31Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-08-20T16:58:40Z"
          },
          {
            "name": "China",
            "updateDate": "2025-08-20T16:58:31Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-08-20T16:57:39Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-20T16:59:03Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-08-20T16:58:25Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-08-20T16:58:53Z"
          },
          {
            "name": "Iran",
            "updateDate": "2025-08-20T16:57:44Z"
          },
          {
            "name": "Israel",
            "updateDate": "2025-08-20T16:57:55Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2025-08-20T16:58:02Z"
          },
          {
            "name": "Military assistance, sales, and agreements",
            "updateDate": "2025-08-20T16:59:15Z"
          },
          {
            "name": "Military operations and strategy",
            "updateDate": "2025-08-20T16:59:37Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-08-20T16:59:24Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-08-20T16:58:47Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-08-20T16:59:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-07-29T21:55:32Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4335ih.xml"
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
      "title": "Abraham Accords Defense Against Terror Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Abraham Accords Defense Against Terror Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide authority to enhance security assistance with countries that are engaged in regional security cooperation efforts in the Middle East and North Africa, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:03:29Z"
    }
  ]
}
```
