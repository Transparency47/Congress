# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7354?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7354
- Title: Stop Underrides Act 2.0
- Congress: 119
- Bill type: HR
- Bill number: 7354
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-04-16T08:06:59Z
- Update date including text: 2026-04-16T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7354",
    "number": "7354",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Stop Underrides Act 2.0",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:59Z",
    "updateDateIncludingText": "2026-04-16T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "WI"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "DE"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "VA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NM"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7354ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7354\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Cohen (for himself, Mr. DeSaulnier , and Ms. Ross ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo reduce the incidence of death by underride by enhancing underride protection on trailers, semitrailers, and single unit trucks, which will result in more survivable truck crashes, to improve motor carrier, passenger motor vehicle, and Vulnerable Road User safety, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Underrides Act 2.0 .\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nunderride crashes involving passenger motor vehicles or Vulnerable Road Users, including motorcyclists, striking and traveling underneath a truck or trailer are a significant public health and safety threat;\n**(2)**\nthe Advisory Committee on Underride Protection established under section 23011(d)(1) of the Infrastructure Investment and Jobs Act ( 49 U.S.C. 30111 note; Public Law 117\u201358 ) has reported that, since the formation of the National Highway Traffic Safety Administration over 50 years ago, 25,100 underrides and 31,500 corresponding fatalities from side underride, rear underride, and front underride crashes have occurred and concluded that no substantial progress has been made by DOT to prevent these horrific crash fatalities and injuries ;\n**(3)**\nthe National Transportation Safety Board has recommended the installation of rear underride guards, side underride guards, and front underride guards on tractor-trailers and rear underride guards and side underride guards on single unit trucks to improve Vulnerable Road User and passenger motor vehicle safety; and\n**(4)**\nthis Act is introduced in memory of the thousands of victims of underride crashes, including\u2014\n**(A)**\nRoya Christine Sadigh, AnnaLeah Karth, Mary Lydia Karth, Sylvia Bingham, Roderick Cota, Moonjohn Kim, Corey Moore, Gregg Williams, Guy Champ Crawford, Carl Hall, Michael Higginbotham, Sandra Maddamma, David Mathis, Mary Katherine Mathis, James Mooney, Christopher Weigl, Bill Zink, David Magnan, Jasen Swift, Samuel Sierra, Brittany McHargue, Christopher Samuel Padilla, Riley Hein, Erin Alexander, Jordan Hensley, Edward Hall, Leslie Rosenberg, Sophie Rosenberg, Ally Davis, Robin Hightman, Alex Wolf, Devyn Killion, Dustin Bosch, Ronald Alleman, Ashley Marie (Walker) Ramirez, Minh-Thi Nguyen, and Melissa Missy De Leon;\n**(B)**\nthose whose catastrophic injuries dramatically changed their lives, including Julie Magnan, Nancy Meuleners, Joshua Rojas, Maiv Yang, Anita Plantage Bomgaars, and Michael B. Hawkins; and\n**(C)**\nthose whose precious lives were cut far too short as a result of preventable underride crashes.\n##### (b) Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto reduce the number of preventable deaths and injuries caused by underride crashes;\n**(2)**\nto ensure the efficacy of comprehensive underride protection systems on roads in the United States; and\n**(3)**\nto improve Vulnerable Road User, motor carrier, and passenger motor vehicle safety.\n#### 3. Definitions\nIn this Act:\n**(1) Commercial motor vehicle**\nThe term commercial motor vehicle has the meaning given the term in section 31132 of title 49, United States Code.\n**(2) Comprehensive underride protection system**\nThe term comprehensive underride protection system means all of the front underride guards, rear underride guards, or side underride guards, as applicable, installed on a commercial motor vehicle.\n**(3) Front underride guard**\nThe term front underride guard means a device installed on or near the front of a commercial motor vehicle that prevents or limits the distance that a vehicle struck by the commercial motor vehicle with the device will slide under the front of the striking commercial motor vehicle.\n**(4) Rear underride guard**\nThe term rear underride guard has the meaning given the term rear impact guard in section 571.223 of title 49, Code of Federal Regulations (or a successor regulation).\n**(5) Title 49 terms**\nThe terms passenger motor vehicle , semitrailer , side underride guard , single unit truck , trailer , and Vulnerable Road User have the meanings given those terms in section 30102(a) of title 49, United States Code.\n#### 4. Amendments to title 49 definitions\n##### (a) In general\nSection 30102(a) of title 49, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraphs (11), (12), and (13) as paragraphs (12), (17), and (19), respectively;\n**(2)**\nby inserting after paragraph (10) the following:\n(11) passenger motor vehicle has the meaning given the term in section 32101. ;\n**(3)**\nby inserting after paragraph (12) (as so redesignated) the following:\n(13) Secretary means the Secretary of Transportation. (14) semitrailer has the meaning given the term in section 571.3(b) of title 49, Code of Federal Regulations (or a successor regulation). (15) side underride guard means a device installed on or near the side of a trailer, semitrailer, or single unit truck that prevents or limits\u2014 (A) the distance that the front end of a vehicle striking the side of the trailer, semitrailer, or single unit truck with the device will slide under the side of the impacted trailer, semitrailer, or single unit truck; and (B) prevents Vulnerable Road Users from sliding under the trailer, semitrailer, or single unit truck with the device. (16) single unit truck means a large commercial truck (excluding any attached trailer). ;\n**(4)**\nby inserting after paragraph (17) (as so redesignated) the following:\n(18) trailer has the meaning given the term in section 571.3(b) of title 49, Code of Federal Regulations (or a successor regulation). ; and\n**(5)**\nby inserting after paragraph (19) (as so redesignated) the following:\n(20) Vulnerable Road User has the meaning given the term vulnerable road user in section 148(a) of title 23. .\n##### (b) Technical amendments\nSection 30102(a) of title 49, United States Code (as amended by subsection (a)), is amended\u2014\n**(1)**\nin each of paragraphs (1) through (18), by striking the period at the end and inserting a semicolon; and\n**(2)**\nin paragraph (19), by striking the period at the end and inserting ; and .\n#### 5. Underride guard rulemaking\n##### (a) In general\nSubchapter II of chapter 301 of title 49, United States Code, is amended by adding at the end the following:\n30130. Side underride guards for trailers, semitrailers, and single unit trucks (a) Rulemaking (1) In general Not later than 18 months after the date of enactment of this section, the Secretary shall finalize regulations that prescribe new or updated motor vehicle safety standards that meet the performance standard described in paragraph (2), including by requiring the installation of side underride guards that meet that performance standard on new trailers, semitrailers, and single unit trucks. (2) Performance standard described The performance standard referred to in paragraphs (1) and (3)(B)(i) is that side underride guards shall\u2014 (A) prevent intrusion into the occupant survival space of a passenger motor vehicle when the passenger motor vehicle is struck, or strikes, perpendicular to a trailer, semitrailer, or single unit truck at any closing speed up to and including 40 miles per hour; (B) impede a Vulnerable Road User from passing underneath a trailer, semitrailer, or single unit truck in an interaction along the side of the trailer, semitrailer, or single unit truck; and (C) contribute to fuel efficiency through the integration of aerodynamic design or components furthering fuel efficiency. (3) Cost-benefit analyses In finalizing regulations under paragraph (1), the Secretary shall consider and calculate in any cost-benefit analysis\u2014 (A) the number of deaths and injuries among passenger motor vehicle occupants and Vulnerable Road Users prevented as a result of those regulations; and (B) net fuel savings, which shall be equal to the difference between\u2014 (i) the cost of fuel expected to be consumed by applicable motor vehicles as a result of the adoption of the performance standard described in paragraph (2); and (ii) the cost of fuel estimated to be consumed by applicable motor vehicles at the existing rate of voluntary adoption of aerodynamic side skirts without side underride guards as of the date on which those regulations are finalized. (b) Compliance The regulations finalized under subsection (a) shall require full compliance with the new or updated motor vehicle safety standards prescribed under that subsection not later than 2 years after the date on which those regulations are finalized. (c) Review of regulations Beginning not later than 5 years after the date on which regulations are finalized under subsection (a), and not less frequently than once every 5 years thereafter, the Secretary shall determine whether any update to the motor vehicle safety standards prescribed under that subsection is necessary to better prevent fatalities caused by underride crashes and improve roadway safety. .\n##### (b) Clarification\nIf the Secretary of Transportation withdraws the advanced notice of proposed rulemaking of the National Highway Traffic Safety Administration entitled Side Underride Guards (88 Fed. Reg. 24535 (April 21, 2023)) before the Secretary of Transportation finalizes regulations in accordance with section 30130(a)(1) of title 49, United States Code (as added by subsection (a)), that withdrawal shall not affect the requirement to finalize regulations in accordance with that section.\n##### (c) Clerical amendments\nThe analysis for chapter 301 of title 49, United States Code, is amended\u2014\n**(1)**\nby striking the item relating to section 30128 and inserting the following:\n30128. Vehicle rollover prevention and crash mitigation. ;\nand\n**(2)**\nby inserting after the item relating to section 30129 the following:\n30130. Side underride guards for trailers, semitrailers, and single unit trucks. .\n#### 6. Advisory Committee on Underride Protection\n##### (a) Reconvening of advisory committee\nNot later than 180 days after the date of enactment of this Act, the Secretary of Transportation shall reconvene the Advisory Committee on Underride Protection established under subsection (d)(1) of section 23011 of the Infrastructure Investment and Jobs Act ( 49 U.S.C. 30111 note; Public Law 117\u201358 ) in accordance with the requirements of that section.\n##### (b) Amendments\nSection 23011(d) of the Infrastructure Investment and Jobs Act ( 49 U.S.C. 30111 note; Public Law 117\u201358 ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), in the matter preceding clause (i), by striking 20 and inserting 22 ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking clause (ix);\n**(ii)**\nby redesignating clause (x) as clause (ix); and\n**(iii)**\nby adding at the end the following:\n(x) Families of underride crash victims who were occupants of a passenger motor vehicle. (xi) Families of underride crash victims who were Vulnerable Road Users (as defined in section 30102(a) of title 49, United States Code). ;\n**(2)**\nin paragraph (4), by striking meet not less frequently than annually and inserting the following: \u201cmeet\u2014\n(A) until final regulations have been promulgated under section 30130(a) of title 49, United States Code\u2014 (i) monthly, via conference call or a virtual meeting platform; and (ii) annually, in person, at the Department of Transportation headquarters; and (B) subsequent to the issuance of the final regulations described in subparagraph (A), not less frequently than annually, in person, at the Department of Transportation headquarters, to assess the status of underride crash protection. ;\n**(3)**\nin paragraph (5), by inserting including deliberative materials, after information, ;\n**(4)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking a biennial and inserting an annual ; and\n**(5)**\nby adding at the end the following:\n(7) Termination date Notwithstanding chapter 10 of title 5, United States Code, the Committee shall terminate on September 30, 2031. .\n#### 7. Publication of underride research, reports, and recommendations\n##### (a) In general\nThe Secretary of Transportation (referred to in this section as the Secretary ) shall publish a publicly accessible website to provide the industry, researchers, advocates, and the public with a repository of underride resources, including\u2014\n**(1)**\nresearch conducted or contracted by the Department of Transportation (referred to in this section as the Department ) on rear underride guards or other rear impact guards;\n**(2)**\nresearch conducted or contracted by the Department on side underride guards or other side impact guards;\n**(3)**\nresearch conducted or contracted by the Department on front underride guards or other front impact guards;\n**(4)**\na link to the database for the Advisory Committee on Underride Protection established under section 23011(d)(1) of the Infrastructure Investment and Jobs Act ( 49 U.S.C. 30111 note; Public Law 117\u201358 ), which shall be updated in a timely manner;\n**(5)**\ninformation and links relating to all underride rulemakings of the Department;\n**(6)**\nstories of victims of underride crashes; and\n**(7)**\ndocumentation of past and ongoing data collection relating to underride crashes.\n##### (b) Updates\nThe Secretary shall update the resources described in subsection (a) not less frequently than quarterly.\n#### 8. NASEM and GAO studies\n##### (a) NASEM study\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation shall seek to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine (referred to in this subsection as the National Academies ) under which the National Academies shall conduct a study on the prevalence of crashes involving the front of large trucks, including the threat of those crashes on Vulnerable Road Users.\n**(2) Report**\nNot later than 180 days after the date on which the National Academies completes the study required under paragraph (1), the National Academies shall submit to Congress a report on the results of the study, which shall include\u2014\n**(A)**\nrecommendations on\u2014\n**(i)**\nhow to better prevent crashes where the front of large trucks contacts a passenger motor vehicle in a manner that causes the passenger motor vehicle to slide under the large truck; and\n**(ii)**\nhow to prevent deaths resulting from those crashes;\n**(B)**\na description of the efficacy of preventative or protective devices on commercial motor vehicles, such as front override guards, in preventing deaths resulting from those crashes; and\n**(C)**\nstatistics, since 2010, describing the prevalence of fatal and non-fatal crashes described in subparagraph (A)(i), including rear underride and side underride crashes, which shall include\u2014\n**(i)**\nthe type, make, and model of vehicles involved in those crashes;\n**(ii)**\nthe types of roads on which those crashes have occurred; and\n**(iii)**\nthe number of fatalities that occurred as a result of those crashes.\n##### (b) GAO study\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States (referred to in this subsection as the Comptroller General ) shall conduct a study on the implementation of the final rule of the National Highway Traffic Safety Administration entitled Federal Motor Vehicle Safety Standards; Rear Impact Guards, Rear Impact Protection (87 Fed. Reg. 42339 (July 15, 2022)).\n**(2) Report**\nNot later than 180 days after the date on which the Comptroller General completes the study required under paragraph (1), the Comptroller General shall submit to the Secretary of Transportation and Congress a report on the results of the study, which shall include\u2014\n**(A)**\nan analysis of the implementation of the final rule described in that paragraph;\n**(B)**\nif applicable, recommendations to the Department of Transportation describing improvements to that final rule or its implementation; and\n**(C)**\nrecommendations to Congress and the Department of Transportation on how to better prevent underrides in crashes occurring at the rear of trailers, semitrailers, and single unit trucks.\n#### 9. FARS review; web-based training for State and local law enforcement\n##### (a) FARS review\nNot later than 1 year after the date of enactment of this Act, the Administrator of the National Highway Traffic Safety Administration (referred to in this section as the Administrator ) shall conduct a review of the Fatality Analysis Reporting System of the National Highway Traffic Safety Administration to determine\u2014\n**(1)**\nthe number of fatalities in crashes reported as an underride crash by State or local law enforcement;\n**(2)**\nthe number of fatalities in crashes that were not reported as an underride crash by State or local law enforcement but should have been reported as an underride crash, as determined by the Administrator after reviewing, with respect to each such crash\u2014\n**(A)**\nthe initial point of impact of the crash, if the crash is a fatal crash involving a large truck;\n**(B)**\nthe Crash Investigation Sampling System of the National Highway Traffic Safety Administration;\n**(C)**\nopen-source media reports with documented photo evidence of an underride occurrence; and\n**(D)**\nany other data and documentation, as determined appropriate by the Administrator; and\n**(3)**\nrecommendations that would improve incident reporting by State and local law enforcement.\n##### (b) Web-Based training\nNot later than 18 months after the date of enactment of this Act, the Administrator shall develop free on-demand, web-based training for State and local law enforcement on how to properly identify and document underride crashes.",
      "versionDate": "2026-02-04",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-02-04",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3775",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Underrides Act 2.0",
      "type": "S"
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-25T16:50:10Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7354ih.xml"
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
      "title": "Stop Underrides Act 2.0",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Underrides Act 2.0",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T07:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reduce the incidence of death by underride by enhancing underride protection on trailers, semitrailers, and single unit trucks, which will result in more survivable truck crashes, to improve motor carrier, passenger motor vehicle, and Vulnerable Road User safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T07:48:28Z"
    }
  ]
}
```
