# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1275?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1275
- Title: Impact Aid Infrastructure Partnership Act
- Congress: 119
- Bill type: S
- Bill number: 1275
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-04-27T14:57:04Z
- Update date including text: 2026-04-27T14:57:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1275",
    "number": "1275",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Impact Aid Infrastructure Partnership Act",
    "type": "S",
    "updateDate": "2026-04-27T14:57:04Z",
    "updateDateIncludingText": "2026-04-27T14:57:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:38:51Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "IL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "AZ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NM"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "HI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MN"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NY"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "AZ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1275is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1275\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Ms. Hirono (for herself, Mr. Blumenthal , Mr. Durbin , Mr. Gallego , Mr. Heinrich , Ms. Klobuchar , Mr. Padilla , Mr. Schatz , Ms. Smith , Mrs. Gillibrand , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide Federal-local community partnership construction funding to local educational agencies eligible to receive payments under the Impact Aid program.\n#### 1. Short title\nThis Act may be cited as the Impact Aid Infrastructure Partnership Act .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nA significant percentage of federally impacted local educational agencies serve schools with facilities that fall far short of meeting basic life-safety standards that ensure a safe learning environment for students and staff alike.\n**(2)**\nThe American Society of Civil Engineers rated school facilities nationally a D+. Many school buildings of schools served by federally impacted local educational agencies were built more than 65 years ago.\n**(3)**\nA 2009 study by the Government Accountability Office found that better school facilities were associated with positive student outcomes in academic achievement, attendance, and higher graduation rates. A second Government Accountability Office study conducted in 2020, concluded that many school facilities of schools served by federally impacted local educational agencies are in need of repair, modernization, renovation, or replacement.\n**(4)**\nData compiled through surveys of federally impacted local educational agencies by both the National Association of Federally Impacted Schools and the National Indian Impacted Schools Association revealed the following:\n**(A)**\n65 percent of respondents indicated their facilities are in fair to poor condition.\n**(B)**\n26 percent of respondents have buildings that are more than 80 years old.\n**(C)**\n53 percent of respondents have no practical capacity to issue bonds.\n**(D)**\n82 percent of respondents identified lack of funds as a reason for delaying construction projects. Construction costs in rural, many times geographically remote, local educational agencies have increased by 30 percent or more in recent years making facility upgrades and replacement even more challenging.\n**(5)**\nLocal educational agencies with some bonding capacity or that have access to other sources of funding are still in need of assistance to improve their buildings to ensure a safe learning environment.\n**(6)**\nFederally impacted local educational agencies located in rural settings have generally higher labor costs and transportation costs for workers and materials that have to be brought to a school construction site than local educational agencies located in an urban setting with school construction costs. Such costs are normally built in by the contractor affecting the total cost of the project.\n**(7)**\nTeacher recruitment and retention is a major challenge for local educational agencies serving students residing on Indian Treaty and Federal trust land as well as land conveyed pursuant to the Alaska Native Claims Settlement Act ( 43 U.S.C. 1601 et seq. ). Because there are no private housing or rental units available to non-Tribal members, the local educational agency must build and maintain rental units. Without local educational agency owned housing, the daily commute can be as much as 90 miles or more each way. One Arizona local educational agency estimated that the cost to rebuild antiquated teacher housing to be $100,000,000.\n**(8)**\nIt is common practice that State educational agencies compile infrastructure needs in the local educational agencies located in the State. For example, the Hawaii Department of Education has identified more than $2,000,000,000 in needed repair, renovation, and construction projects to address\u2014\n**(A)**\nstructural and health and safety needs;\n**(B)**\ncompliance with the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) and title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ); and\n**(C)**\nvarious other infrastructure and construction needs.\n##### (b) Purposes\nThe purpose of this Act is to provide a collaborative Federal-local community partnership that will provide both Federal and local funding to address the facility needs of federally impacted local educational agencies. The partnership shall be designed to\u2014\n**(1)**\nprovide formula grants to federally impacted local educational agencies that have no capacity to issue bonds because of the presence of large parcels of non-taxable Federal property;\n**(2)**\nprovide partnership grants requiring a local match to local educational agencies that have a limited capacity to provide facility funding;\n**(3)**\nbase local matching dollars on the learning opportunity threshold total percentage, as described in subparagraph (B)(i) of section 7003(b)(3) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7703(b)(3) ); and\n**(4)**\nprovide grants under section 7007(a) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7707(a) ) to address local educational agency needs to modernize and provide basic building improvements.\n#### 3. Impact aid construction grants authorized\n##### (a) Funding and sunset\n**(1) Authorization of appropriations**\n**(A) In general**\nThere are authorized to be appropriated $250,000,000 for the first fiscal year that begins after the date of enactment of this Act, and each of the 3 succeeding fiscal years.\n**(B) Designation**\nOf the amount appropriated for each fiscal year, the Secretary of Education shall designate\u2014\n**(i)**\n75 percent for competitive grants awarded under section 4; and\n**(ii)**\n25 percent for formula grants awarded under section 5.\n**(2) Supplemental funding**\nThe amount authorized under paragraph (1) shall be in addition to any amounts authorized to be appropriated or otherwise made available to carry out section 7007 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7707 ).\n**(3) Availability of funds**\nAny amounts appropriated under paragraph (1) shall remain available until expended.\n**(4) Sunset**\nThe authority to award grants under this Act shall expire at the end of the 4-year period beginning on the date in which funds are first made available to award a grant under this Act.\n##### (b) Reservation for technical assistance, management, and oversight\nFrom the funds appropriated under subsection (a)(1), the Secretary of Education may reserve not more than half of 1 percent for technical assistance, management, and oversight of the activities carried out with those funds.\n#### 4. Competitive grant awards based on facility condition\nThe Secretary of Education shall, based on applications submitted by local educational agencies under section 6 and eligible for payments under section 7002 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7702 ) or section 7003 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7703 ), establish a facility condition priority listing for grant awards as follows:\n**(1) Emergency grants priority one**\nThe Secretary of Education shall award grants, on a competitive basis, by first identifying those local educational agencies\u2014\n**(A)**\nthat have a facility\u2014\n**(i)**\nas certified by a State, county, city, or Tribal official or a licensed architect or engineer, that is in violation of a Federal, State, county, city, or Tribal building code representing a health hazard to students and school personnel;\n**(ii)**\nthat fails to meet building and classroom standards to ensure the health and safety of students and staff, as set by the Centers for Disease Control and Prevention, requiring classroom building modification or replacement to\u2014\n**(I)**\nensure quality ventilation systems;\n**(II)**\nensure classroom space to reduce class sizes and ensure social distancing guidelines when required;\n**(III)**\naddress structural deficiencies; and\n**(IV)**\naddress other health, safety, and environmental conditions that would impact the health, safety, and learning ability of students;\n**(iii)**\nthat is not in compliance with meeting student capacity standards as required by the State, including failure to meet accessibility standards for persons with disabilities; or\n**(iv)**\nthat lacks adequate service capacity or infrastructure necessary to utilize technology to offer a curriculum that meets the current academic standards in the State in which the local educational agency is located; or\n**(B)**\nin the case of local educational agencies eligible for payments under section 7003(a)(1)(C) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7703(a)(1)(C) ), that have teacher housing that is in need of repair or new construction to meet the needs of school personnel residing in such housing.\n**(2) Emergency grants priority two**\nAfter identifying those local educational agencies as described in paragraph (1) for priority in grant awards, the Secretary of Education shall then award grants, on a competitive basis, by identifying those local educational agencies that\u2014\n**(A)**\nhave a facility that\u2014\n**(i)**\ndoes not meet minimum structural or health and safety standards as adopted by the American Society of Civil Engineers and is considered to be in poor condition and represents a potential health or safety hazard to students and school personnel, including due to\u2014\n**(I)**\npoor indoor air quality;\n**(II)**\nthe presence of hazardous and toxic substances and chemicals;\n**(III)**\nthe lack of safe drinking water at the tap and water used for meal preparation, including due to the level of lead and other contaminants in such water;\n**(IV)**\nenergy and water inefficiency;\n**(V)**\nexcessive classroom noise;\n**(VI)**\nstructural deficiencies; or\n**(VII)**\nother health, safety, and environmental conditions that would impact the health, safety, and learning ability of students;\n**(ii)**\nis not in compliance with meeting student capacity standards as required by the State, including failure to meet accessibility standards for persons with disabilities; or\n**(iii)**\nlacks adequate services necessary to utilize technology to offer a curriculum that meets the current academic standards in the State in which the local educational agency is located; or\n**(B)**\nin the case of local educational agencies eligible for payments under section 7003(a)(1)(C) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7703(a)(1)(C) ), have an identified need for teacher housing to ensure a safe living environment for teachers and their families or a need for repair of existing housing or new construction to meet the basic needs of school personnel residing in such housing.\n#### 5. Formula grants\nFrom funds designated under section 3(a)(1)(B)(ii), the Secretary of Education shall make payments in accordance with section 7007(a) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7707(a) ), except that\u2014\n**(1)**\nwhen calculating the total number of weighted student units as described in paragraph (3)(A)(i)(II) of section 7007(a) of the Elementary and Secondary Education of 1965 ( 20 U.S.C. 7707(a) ), the Secretary of Education shall also include the total number of weighted student units of children described in subparagraphs (B) and (D)(i) of section 7003(a)(1) of such Act for the preceding year for all local educational agencies not meeting the requirements as described in section 7007(a)(2)(B) of such Act but that meet the requirements of section 572(a)(2) of the National Defense Authorization Act for Fiscal Year 2006 ( 20 U.S.C. 7703b(a)(2) ); and\n**(2)**\nwhen calculating the total number of weighted student units as described in section 7003(a)(1)(C) of the Elementary and Secondary Education of 1965 ( 20 U.S.C. 7703(a)(1)(C) ), the Secretary of Education shall also include the number of children determined under section 7003(a)(1)(C) of such Act for the preceding school year that constituted at least 20 percent of the total student enrollment in the schools of the agency during the preceding school year.\n#### 6. Application\nA local educational agency eligible to apply for a grant section 4 that desires to receive a grant shall submit an application at such a time and containing such information as determined appropriate by the Secretary of Education.\n#### 7. Award criteria\nWhen awarding a grant under section 4, the Secretary of Education shall first apply the facility condition priority listing established under such section, and after such priority requirements are applied, the Secretary of Education shall then\u2014\n**(1)**\nfirst consider those local educational agencies (or, in the case of a local educational agency that does not have the authority to tax or issue bonds, the agency\u2019s fiscal agent) that have limited or no capacity to issue bonds or have a total assessed value of real property that may be taxed for school purposes of less than $50,000,000;\n**(2)**\nnext consider those local educational agencies not described in paragraph (1) that\u2014\n**(A)**\nhave a total assessed value of real property that may be taxed for school purposes of less than $100,000,000; or\n**(B)**\nhave an assessed value of real property that may be taxed for school purposes per student that is less than the average of the assessed value of real property that may be taxed for school purposes per student in the State in which the local educational agency is located; and\n**(3)**\nfinally consider\u2014\n**(A)**\nthe number and percentages of children described in subparagraphs (A), (B), (C), and (D) of section 7003(a)(1) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7703(a)(1) ) enrolled in the school facility to be supported with grant funds;\n**(B)**\nthe learning opportunity threshold total percentage as described in subparagraph (B)(i) of section 7003(b)(3) of such Act ( 20 U.S.C. 7703(b)(3) );\n**(C)**\nwith respect to local educational agencies eligible for payments under section 7002 of such Act ( 20 U.S.C. 7702 ), the percentage of land in the local educational agency that is Federal property;\n**(D)**\nthe potential use for community programs and events in the school facility to be supported with grant funds;\n**(E)**\nthe feasibility of project completion within 24 months from the grant award; and\n**(F)**\nthe availability of other resources for the proposed project including the use of in-kind contributions.\n#### 8. Payments\n##### (a) In general\nWhen making payments for grants awarded under this Act, the Secretary of Education shall comply with the following:\n**(1)**\nMake payment as required in full for those local educational agencies described in section 4(1) with no capacity to issue bonds.\n**(2)**\nRequire those local educational agencies not described in paragraph (1) to pay a percentage of the total cost of the project supported with grant funds as follows:\n**(A)**\nFor those local educational agencies with a learning opportunity threshold total percentage, as described in subparagraph (B)(i) of section 7003(b)(3) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7703(b)(3) )\u2014\n**(i)**\nthat is 80 percent or greater, such agencies shall pay a non-Federal share equal to 10 percent of the total cost of the project;\n**(ii)**\nthat is less than 80 percent, but 50 percent or greater, such agencies shall pay a non-Federal share equal to 20 percent of the total cost of the project; and\n**(iii)**\nthat is less than 50 percent, such agencies shall pay a non-Federal share equal to 25 percent of the total cost of the project.\n**(B)**\nFor those local educational agencies eligible to receive a payment under section 7002 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7702 ) that are not described in paragraph (1) of section 4, such agencies shall pay a non-Federal share equal to 25 percent of the total cost of the project.\n**(3)**\nMake payment as required in full for those local educational agencies described in paragraph (1) or (2) of section 4, whose payment is $5,000,000 or less for the year in which they are to receive the grant.\n**(4)**\nMake payment to those local educational agencies described in paragraph (1) or (2) of section 4, whose payment is more than $5,000,000 for the year in which they are to receive the grant, after final drawings and specifications have been approved by the Secretary of Education and the construction contract has been entered into, in accordance with requirements as determined by the Secretary of Education and at such times and in such installments as may be reasonable.\n##### (b) Redistribution of payments\nAny funds paid to a local educational agency under this Act and not expended, by such a time as determined by the Secretary of Education, for the purposes for which such funds are paid shall be redistributed to make payments under section 7007(a) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7707(a) ).\n#### 9. General provisions\n##### (a) Use of funds\n**(1) Authorized activities**\nGrant funds under this Act may be used for one or more of the following:\n**(A)**\nConstruction.\n**(B)**\nRenovation.\n**(C)**\nRepair of school facilities.\n**(2) In-kind contributions**\nA local educational agency may use in-kind contributions to meet the non-Federal share requirement under section 8(a)(2).\n**(3) Prohibitions on use of funds**\nA local educational agency may not use a grant awarded under paragraph (1) or (2) of section 4 for\u2014\n**(A)**\na project for a school facility for which the agency does not have\u2014\n**(i)**\nfull title;\n**(ii)**\na long-term Tribal lease agreement; or\n**(iii)**\nanother interest as defined in regulation by the Secretary of Education; and\n**(B)**\nthe acquisition of real property.\n**(4) Supplement, not supplant**\nA local educational agency shall use funds awarded under this Act only to supplement the amount of funds that would, in the absence of the Federal funds provided under the grant, be made available from non-Federal sources to carry out construction, renovation, or repairs of school facilities as described in this Act and not to supplant such funds.\n##### (b) Annual report on grant program\nNot later than September 30 of the first fiscal year that begins after the Secretary of Education first awards grants under this Act and each fiscal year thereafter, the Secretary of Education shall submit to the appropriate congressional committees, and make publicly available, a report on the projects carried out with funds made available under this Act.\n##### (c) Carry-Over of certain applications\n**(1) In general**\nA local educational agency that applies for a grant under this Act for a fiscal year and does not receive the grant for the fiscal year shall have the application for the grant considered for the following fiscal year not to exceed the end of the 4-year period as described in paragraph (4) of section 3(a), subject to the priority requirements of paragraphs (1) and (2) of section 4.\n**(2) Priority listing**\nThe Secretary of Education shall\u2014\n**(A)**\nmaintain a priority listing of local educational agencies meeting the eligibility requirements found in\u2014\n**(i)**\nparagraph (1) of section 4; and\n**(ii)**\nparagraph (2) of section 4; and\n**(B)**\nupdate the listing for each of paragraphs (1) and (2) of section (4), including those local educational agencies that applied for the previous fiscal year, but were not funded and for those agencies applying the succeeding fiscal year.\n##### (d) Local educational agency defined\nIn this Act, the term local educational agency has the meaning given the term in section 7013 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7713 ).",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-03",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2629",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Impact Aid Infrastructure Partnership Act",
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
            "name": "Air quality",
            "updateDate": "2026-04-27T14:56:44Z"
          },
          {
            "name": "Building construction",
            "updateDate": "2026-04-27T14:56:56Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-27T14:57:03Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2026-04-27T14:56:32Z"
          },
          {
            "name": "Educational facilities and institutions",
            "updateDate": "2026-04-27T14:56:28Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-04-27T14:56:21Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2026-04-27T14:56:38Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2026-04-27T14:56:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-05-01T15:49:52Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1275is.xml"
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
      "title": "Impact Aid Infrastructure Partnership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T11:48:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Impact Aid Infrastructure Partnership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide Federal-local community partnership construction funding to local educational agencies eligible to receive payments under the Impact Aid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:25Z"
    }
  ]
}
```
