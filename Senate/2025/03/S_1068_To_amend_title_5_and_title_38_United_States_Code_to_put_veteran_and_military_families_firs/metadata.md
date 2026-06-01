# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1068?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1068
- Title: Putting Veterans First Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1068
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-05-08T13:52:59Z
- Update date including text: 2025-05-08T13:52:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1068",
    "number": "1068",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Putting Veterans First Act of 2025",
    "type": "S",
    "updateDate": "2025-05-08T13:52:59Z",
    "updateDateIncludingText": "2025-05-08T13:52:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T23:25:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-13",
      "state": "VT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NY"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "AZ"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "VA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NV"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NV"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "CA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "OR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "MN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "CA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "HI"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "AZ"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NJ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NM"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "RI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Lujan",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "CO"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "MD"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1068is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1068\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Blumenthal (for himself, Mr. Sanders , Ms. Duckworth , Mrs. Gillibrand , Mr. Gallego , Mr. Kaine , Ms. Rosen , Ms. Cortez Masto , Mr. Schiff , Mr. Merkley , Ms. Klobuchar , Mr. Padilla , Ms. Hirono , Mr. Kelly , Mr. Booker , Mr. Heinrich , Mr. Whitehouse , Mr. Luj\u00e1n , Mr. Hickenlooper , Mr. Wyden , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 5 and title 38, United States Code, to put veteran and military families first and to provide protections for employees, benefits, and programs of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Putting Veterans First Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Putting veteran and military families first\nSec. 101. Reinstatement of members of the military community who were Federal employees.\nSec. 102. Protection for members of the military community who were Federal employees.\nSec. 103. Report on members of the military community in the civil service.\nSec. 104. Comptroller General report on military community employment.\nTITLE II\u2014Department of Veterans Affairs employees\nSubtitle A\u2014Protections\nSec. 201. Limitations on hiring freezes at Department of Veterans Affairs.\nSec. 202. Limitations on closing offices at Department of Veterans Affairs.\nSec. 203. Limitations on changes to telework and remote work at Department of Veterans Affairs.\nSec. 204. Limitations on changes to final job offers at Department of Veterans Affairs.\nSubtitle B\u2014Reporting\nSec. 205. Notice and justification required before reduction in force at Department of Veterans Affairs.\nSec. 206. Department of Veterans Affairs personnel reporting.\nSec. 207. Department of Veterans Affairs research personnel reporting.\nSec. 208. Prohibition on individuals serving as Secretary of Veterans Affairs from also serving as heads of other Federal agencies.\nSec. 209. Office of Special Counsel.\nSec. 210. Office of Government Ethics.\nSubtitle C\u2014Restoring accountability and services\nSec. 211. Report on effects of removing essential programs, offices, and services from Department of Veterans Affairs.\nSec. 212. Restoring Department of Veterans Affairs programs, offices, and services affected since the beginning of the second Trump Administration.\nTITLE III\u2014Protections for civil servants\nSec. 301. Nominations to Merit Systems Protection Board.\nSec. 302. Modifications to appeal rights for probationary employees.\nSec. 303. Authority to retract offers and contracts relating to deferred resignations.\nSec. 304. Limitation on changes to competitive service categories of positions.\nTITLE IV\u2014Mental health care for civil servants\nSec. 401. Mental health services.\nSec. 402. Mental health services for current civil servants.\nTITLE V\u2014Employment assistance for civil servants\nSec. 501. Employment assistance.\nSec. 502. Office of Personnel Management and the Department of Labor work on employment opportunities for members of the military community.\nTITLE VI\u2014Department of Government Efficiency\nSec. 601. Limitation on access to veteran and department information, systems, and data.\nSec. 602. Limitation on application of certain Executive Orders relating to Department of Government Efficiency at Department of Veterans Affairs.\nSec. 603. Report on compliance with limitation on access to veteran and Department of Veterans Affairs information, systems, and data and Inspector General review.\nTITLE VII\u2014Financial needs of the Department of Veterans Affairs\nSec. 701. Definition; rule of construction.\nSec. 702. Report on financial effect of the Department of Government Efficiency on the Department of Veterans Affairs.\nSec. 703. Reinstatement of contracts and review of mass contract cancellations.\nSec. 704. Limitations on mass contract cancellations.\nSec. 705. Charge card program of the Department of Veterans Affairs.\nTITLE VIII\u2014Reporting requirements\nSec. 801. Requirement for Veterans Benefits Administration Monday Morning Workload Report.\nSec. 802. Improvements regarding periodic publication of metrics relating to processing of appeals.\nSec. 803. Publication of wait times for community care from Department of Veterans Affairs.\nSec. 804. Period for Secretary of Veterans Affairs to respond to questions submitted by members of certain congressional committees.\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given that term in section 3330d of title 5, United States Code.\n**(2) Caregiver**\nThe term caregiver means an adult family member or other individual who has a significant relationship with, and who provides a broad range of assistance to, a wounded, ill, injured, or disabled member of the Armed Forces or veteran or a dependent of such a member or veteran with a chronic or other health condition, disability, or functional limitation.\n**(3) Civil service**\nThe term civil service has the meaning given that term in section 2101 of title 5, United States Code.\n**(4) Demotion**\nThe term demotion means a reduction in grade (as defined in section 7511(a) of title 5, United States Code).\n**(5) Member of the armed forces**\nThe term member of the armed forces has the meaning given that term in 315.612(b)(4) of title 5, Code of Federal Regulations, or any successor thereto.\n**(6) Military spouse**\nThe term military spouse means\u2014\n**(A)**\nthe husband or wife of a member of the armed forces;\n**(B)**\nthe husband or wife of a retired, totally disabled, or separated member of the armed forces; or\n**(C)**\nthe widow or widower of a member of the armed forces killed while performing active duty or who died from a service-connected injury or illness.\n**(7) Removal**\nThe term removal means removing an individual from the civil service.\n**(8) Reserve component**\nThe term reserve component has the meaning given that term in section 101 of title 38, United States Code.\n**(9) Suspension**\nThe term suspension means the placing an individual in a temporary status without duties and pay for a period of longer than 7 days.\n**(10) Survivor**\nThe term survivor means a family member of a member of the armed forces or veteran who died while on active duty or after military retirement or of a service-connected injury or illness.\n**(11) Veteran**\n**(A) In general**\nExcept as provided in subparagraph (B), the term veteran means a person who served on active duty as a member of the armed forces, regardless of length of service, and who was discharged or released therefrom.\n**(B) Exclusions**\nThe term veteran does not include a person who\u2014\n**(i)**\nreceived a dishonorable discharge from the Armed Forces; or\n**(ii)**\nwas discharged or dismissed from the Armed Forces by reason of the sentence of a general court-martial.\nI\nPutting veteran and military families first\n#### 101. Reinstatement of members of the military community who were Federal employees\n##### (a) In general\nAny removal, demotion, or suspension of a veteran, military spouse, caregiver, survivor, or member of a reserve component who was serving in a position in the civil service that occurred during the period beginning on January 20, 2025, and ending on the date of enactment of this Act shall have no force or effect.\n##### (b) Back pay and resumption of benefits\nAny person whose removal, demotion, or suspension is rendered without force or effect under subsection (a) shall\u2014\n**(1)**\nreceive back pay for any pay not received by the person during the period beginning on the date of the removal, suspension, or demotion and ending on the date of enactment of this Act; and\n**(2)**\nhave benefits restored, retroactive to the date of the removal, demotion, or suspension.\n##### (c) Election To resign\nAt the election of a person whose removal, demotion, or suspension is rendered without force or effect under subsection (a), at any time after the date of enactment of this Act, the person may resign from the position of the person in the civil service, which shall not affect the obligation to provide back pay or the resumption of benefits with respect to the period beginning on the date of the removal, demotion, or suspension and ending on the date of enactment of this Act.\n#### 102. Protection for members of the military community who were Federal employees\n##### (a) In general\nAny veteran, military spouse, caregiver, survivor, or member of a reserve component who is in a position in the civil service may not be removed, demoted, or suspended\u2014\n**(1)**\nas a part of a group of more than 5 persons who are being removed, demoted, or suspended on the same day by the agency employing the persons;\n**(2)**\nwithout providing a notification to the direct supervisor of the veteran, military spouse, caregiver, survivor, or member of a reserve component not less than 10 business days before the removal, demotion, or suspension, unless the supervisor advises or approves the removal, demotion, or suspension;\n**(3)**\non the basis of performance, unless the veteran, military spouse, caregiver, survivor, or member of a reserve component has received at least 1 performance rating at or below level 2 or minimally satisfactory (or a similar equivalent level) during the 1-year period ending on the date of the removal, demotion, or suspension; or\n**(4)**\nif the removal, demotion, or suspension would result in a greater than 50 percent vacancy rate for the office or position of the veteran, military spouse, caregiver, survivor, or member of a reserve component or a significant reduction or elimination of the duties being carried out by the veteran, military spouse, caregiver, survivor, or member of a reserve component, without approval by the direct supervisor of the veteran, military spouse, caregiver, survivor, or member of a reserve component.\n##### (b) Review\nNot later than 10 days after the date of the removal, demotion, or suspension of any veteran, military spouse, caregiver, survivor, or member of a reserve component in a position the civil service, the removal, demotion, or suspension shall be referred to the Merit Systems Protection Board or the Office of Special Counsel, unless the individual agrees to waive the right to such a referral.\n#### 103. Report on members of the military community in the civil service\nNot later than 90 days after the date of enactment of this Act, and not later than 90 days after the end of each fiscal year thereafter, each agency shall submit to the Committee on Veterans\u2019 Affairs, the Committee on Armed Services, the Committee on Appropriations, and the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Veterans\u2019 Affairs, the Committee on Armed Services, the Committee on Appropriations, and the Committee on Homeland Security of the House of Representatives the following information:\n**(1)**\nThe number of veterans, military spouses, caregivers, survivors, and members of a reserve component who, during the prior fiscal year\u2014\n**(A)**\nwere hired by the agency, disaggregated by those who were serving at a different agency immediately before being hired by the agency and those hired from outside the Federal Government;\n**(B)**\nseparated from service with the agency, disaggregated by those who were hired by another agency and those who were not hired by another agency; or\n**(C)**\nwere removed by the agency.\n**(2)**\nThe number of veterans, military spouses, caregivers, survivors, and members of a reserve component who, as of the end of the prior fiscal year, were employed by the agency.\n**(3)**\nData regarding any directed efforts or incentives utilized to recruit or retain veterans, military spouses, caregivers, survivors, and members of a reserve component during the prior fiscal year.\n**(4)**\nFor the second report under this section, and each report thereafter, data on changes to the number of veterans, military spouses, caregivers, survivors, or members of a reserve component hired by, separated from, or were employed by the agency, as compared to the most recent report.\n#### 104. Comptroller General report on military community employment\nNot later than April 1, 2027, the Comptroller General of the United States shall submit to the Committee on Veterans\u2019 Affairs, the Committee on Appropriations, the Committee on Armed Services, and the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Veterans\u2019 Affairs, the Committee on Appropriations, the Committee on Armed Services, and the Committee on Homeland Security of the House of Representatives and publicly issue a report regarding employment of military community members by the Federal Government, which shall\u2014\n**(1)**\ninclude a review of employment of veterans, military spouses, caregivers, survivors, and members of a reserve component by the Federal Government during fiscal years 2024 and 2025;\n**(2)**\nreview the period of service in positions in the civil service by veterans, military spouses, caregivers, survivors, and members of a reserve component and the rate of removal, suspension, or demotion of veterans, military spouses, caregivers, survivors, and members of a reserve component from positions in the civil service, as compared to other individuals in positions in the civil service; and\n**(3)**\ndescribe any changes in employment of veterans, military spouses, caregivers, survivors, and members of a reserve component across agencies between the end of fiscal year 2024 and the end of fiscal year 2025.\nII\nDepartment of Veterans Affairs employees\nA\nProtections\n#### 201. Limitations on hiring freezes at Department of Veterans Affairs\n##### (a) Limitation\nNeither a position nor an employee at the Department of Veterans Affairs may be subject to a hiring freeze, hiring prohibition, or similar policy\u2014\n**(1)**\nunless the Secretary determines that unfilled positions or lack of staff subject to such a freeze will not result in increased costs to the Department; and\n**(2)**\nuntil the date that is 90 days after the date that the Secretary of Veterans Affairs submits a report regarding the hiring freeze pursuant to subsection (b).\n##### (b) Report\nBefore issuing any hiring freeze, hiring prohibition, or similar policy, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the hiring strategy of the Secretary and budgetary proof that such a freeze, hiring prohibition, or similar policy will not cause increased costs to the Department.\n#### 202. Limitations on closing offices at Department of Veterans Affairs\n##### (a) Prohibition\nThe Secretary of Veterans Affairs may not remove, close, or realign any office or program of the Department of Veterans Affairs except pursuant to a provision of law that specifically authorizes such removal, closure, or realignment.\n##### (b) Notification required\nWhenever the Secretary removes, closes, or realigns an office or program of the Department, the Secretary shall, not later than 1 year before the date on which the Secretary commences such removal, closure, or realignment, submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives notice of the intent of the Secretary to carry out such removal, closure, or realignment.\n##### (c) Assistance for displaced employees\nIn any case in which an employee of the Department is displaced by the removal, closure, or realignment of an office or program of the Department, the Secretary shall make a significant effort to find another employment opportunity for the employee within the Department.\n#### 203. Limitations on changes to telework and remote work at Department of Veterans Affairs\n##### (a) Notice required\nThe Secretary of Veterans Affairs may not take any action to change to a telework or remote work policy of the Department of Veterans Affairs until after the date that is 1 year after the date on which the Secretary\u2014\n**(1)**\nsubmits to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives notice of the intent of the Secretary to take such action or make such change; and\n**(2)**\ntransmits notice of such intent to the following:\n**(A)**\nLabor organizations that represent employees of the Department.\n**(B)**\nThe employees of the Department who would be affected by such action or change.\n##### (b) Enforcement\nA violation of subsection (a) against an employee of the Department of Veterans Affairs shall be treated, under section 505 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794a ), as a violation of section 501 of the Rehabilitation Act of 1973 ( 29 U.S.C. 791 ) against an aggrieved employee described in subsection (a) of that section.\n#### 204. Limitations on changes to final job offers at Department of Veterans Affairs\n##### (a) Limitations\nThe Secretary of Veterans Affairs may not rescind or make any change to a final offer of employment with the Department of Veterans Affairs for any reason that is not directly related to an action or quality of the individual to whom the offer of employment was extended.\n##### (b) Remedies\nA rescission or change made in violation of subsection (a) may be appealed to the Merit Systems Protection Board in accordance with the procedures under section 7701 of title 5, United States Code.\nB\nReporting\n#### 205. Notice and justification required before reduction in force at Department of Veterans Affairs\n##### (a) In general\nNot later than 180 days before commencing any effort to carry out a reduction in force, or similar action under a different name, at the Department of Veterans Affairs, the Secretary of Veterans Affairs shall submit a justification for the reduction in force or similar action to the following:\n**(1)**\nThe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the Senate.\n**(2)**\nThe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the House of Representatives.\n**(3)**\nThe labor organizations that represent employees of the Department.\n**(4)**\nEach employee of the Department who will be affected by the reduction in force or similar action.\n##### (b) Contents\nEach justification submitted pursuant to subsection (a) for a reduction in force or similar action shall include the following:\n**(1)**\nFor each employee or position that will be terminated pursuant to the reduction in force or similar action, the following:\n**(A)**\nDocumentation and analysis used to determine that the termination will not reduce or negatively affect delivery of care or benefits for veterans.\n**(B)**\nDocumentation and analysis used to determine that the termination will not cost the Department or the Federal Government more than if the Department were to retain the position or employee.\n**(C)**\nCost estimate, strategic plan, analysis, and any other relevant information or documentation the Secretary used to determine the need to terminate the employee or position.\n**(2)**\nThe planned timeline for the reduction in force or similar action and the methodology the Secretary will use to track the actual effects of the reduction in force or similar action.\n**(3)**\nOptions for changing the plans of the Secretary and a strategy should an unexpected negative impact to veterans occur from the planned actions.\n#### 206. Department of Veterans Affairs personnel reporting\n##### (a) In general\nSection 505 of the John S. McCain III, Daniel K. Akaka, and Samuel R. Johnson VA Maintaining Internal Systems and Strengthening Integrated Outside Networks Act of 2018 ( Public Law 115\u2013182 ; 38 U.S.C. 301 note) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter before subparagraph (A), by striking information, and all that follows through facility: and inserting information: ;\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby inserting (i) before The number ; and\n**(II)**\nby adding at the end the following new clause:\n(ii) Information made available under this subparagraph shall be updated not less frequently than once each quarter to account for delays in data processing and shall reflect the most recently available data. ;\n**(iii)**\nin subparagraph (C), by striking vacancies, by occupation. and inserting positions currently undergoing a recruitment action, disaggregated by occupation and by stage of recruitment, including Manager Request Initiation Stage, recruitment stage, onboarding stage, and waiting to start stage, or successor stages if modified. ;\n**(iv)**\nin subparagraph (E)(iii), by striking potential hires or ; and\n**(v)**\nby adding at the end the following new subparagraph:\n(F) The number of positions vacated during the quarter for which the Department has not initiated a recruitment action, including the date the position was vacated, disaggregated by occupation. ;\n**(B)**\nby redesignating paragraph (5) as paragraph (6);\n**(C)**\nby inserting after paragraph (4) the following new paragraph (5):\n(5) Display of information The display of information made publicly available on an internet website of the Department pursuant to paragraph (1), shall be disaggregated\u2014 (A) by departmental component; (B) in the case of information relating to Veterans Health Administration positions, by medical facility; and (C) in the case of information relating to Veterans Benefits Administration positions, by regional office. ; and\n**(D)**\nin paragraph (6), as redesignated by subparagraph (B), by striking shall and all that follows and inserting \u201cshall\u2014\n(A) review the administration of the website required under paragraph (1); (B) develop recommendations relating to the improvement of such administration; and (C) submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report containing\u2014 (i) the findings of the Inspector General with respect to the most recent review conducted under subparagraph (A); and (ii) the recommendations most recently developed under subparagraph (B). ; and\n**(2)**\nby amending subsection (b) to read as follows:\n(b) Annual report Each year, the Secretary shall submit to Congress an annual report that includes the following: (1) A description of the steps the Department is taking to achieve full staffing capacity. (2) A description of the actions the Department is taking to improve the onboard timeline for facilities of the Department, including\u2014 (A) in the case of facilities of the Veterans Health Administration, for facilities for which the duration of the onboarding process exceeds the metrics laid out in the Time to Hire Model of the Veterans Health Administration, or successor model; and (B) in the case of the Veterans Benefits Administration, for regional offices that exceed the time-to-hire target of the Office of Personnel Management. (3) The amount of additional funds necessary to enable the Department to reach full staffing capacity. (4) Such recommendations for legislative or administrative action as the Secretary may have in order to achieve full staffing capacity at the Department. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date of the enactment of this Act and shall apply with respect to the first update under section 505(a)(3) of such Act beginning after the date of the enactment of this Act and each update thereafter.\n#### 207. Department of Veterans Affairs research personnel reporting\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Congress a report that includes\u2014\n**(1)**\nthe number of Department of Veterans Affairs research employees who were terminated from the Department since January 20, 2025;\n**(2)**\nthe number of Department research employees who had their term limits shortened since January 20, 2025; and\n**(3)**\na list of the research studies the employees described in paragraphs (1) and (2) were working on.\n#### 208. Prohibition on individuals serving as Secretary of Veterans Affairs from also serving as heads of other Federal agencies\n##### (a) In general\nSection 303 of title 38, United States Code, is amended\u2014\n**(1)**\nby striking There is and inserting the following:\n(a) In general There is ; and\n**(2)**\nby adding at the end the following new subsections:\n(b) Prohibition (1) In general Notwithstanding any other provision of law, including any provision of subchapter III of chapter 33 of title 5, an individual who is serving as the Secretary, regardless of whether such service is pursuant to an appointment made by and with the advice and consent of the Senate or such service is in an acting capacity, may not serve as the head of any other Executive agency, either pursuant to an appointment made by and with the advice and consent of the Senate or in an acting capacity, while serving as the Secretary. (2) Effect of noncompliance (A) Removal from office An individual serving as the Secretary who is not in compliance with subsection (a) is hereby removed from the position of Secretary. (B) Prohibition on certain actions An individual removed from the position of Secretary by subparagraph (A) may not issue orders, guidance, direct any people or resources, or in any other manner carry out any of the functions of the Secretary. (C) Treatment of orders, guidance, and direction Any order, guidance, or direction of people or resources or any other leadership action issued by an individual who was removed from the position of Secretary by subparagraph (A) and that was issued on or after the date of such removal shall be considered unlawful. (c) Definition of Executive agency In this section, the term Executive agency has the meaning given such term in section 105 of title 5 and includes the Office of Government Ethics and the Office of Special Counsel, but does not include any advisory committee (as such term is defined in section 1001 of title 5). .\n##### (b) Effective date\nSubsections (b) and (c) of section 303 of such title, as added by subsection (a), shall take effect on the date that is 7 days after the date of the enactment of this Act.\n##### (c) Report\n**(1) In general**\nNot later than 30 days after the date specified in subsection (b), the most senior career individual in the Office of the General Counsel of the Department of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on compliance with the provisions of this Act.\n**(2) Contents**\nThe report submitted pursuant to paragraph (1) shall include the following:\n**(A)**\nDocumentation as to whether the Secretary of Veterans Affairs is in compliance with section 303(b) of title 38, United States Code, as added by subsection (a).\n**(B)**\nA description of the procedures in effect to reestablish firewalls, conflict of interest protections, and independence requirements at the Department of Veterans Affairs.\n**(C)**\nAn affirmation that the Department of Veterans Affairs will comply with and respect the independent oversight and investigative power of the Office of Special Counsel, the Office of Government Ethics, the Merit Systems Protection Board, the Government Accountability Office, the Office of Inspector General of the Department of Veterans Affairs, the Federal Labor Relations Board, and all other relevant investigatory and audit bodies.\n#### 209. Office of Special Counsel\nSection 1211(b) of title 5, United States Code, is amended by striking the sixth sentence and inserting the following: The Special Counsel, including any individual serving as the Special Counsel in an acting capacity, may not hold another office or position in the Government of the United States while serving as the Special Counsel. Notwithstanding any provision of subchapter III of chapter 33, if the Special Counsel dies, resigns, or is otherwise unable to perform the functions and duties of the office, the most senior career attorney serving in the Office of General Counsel of the Office of Special Counsel, as of the date of the death, resignation, or beginning of inability to serve, shall serve as the Special Counsel until an individual is appointed by the President as the Special Counsel in accordance with this subsection. .\n#### 210. Office of Government Ethics\nSection 13121(b) of title 5, United States Code, is amended\u2014\n**(1)**\nby striking There shall and inserting the following:\n(1) In general There shall ; and\n**(2)**\nby adding at the end the following:\n(2) Removal or transfer The Director may only be removed from office by the President for inefficiency, neglect of duty, or malfeasance in office. (3) Restriction on holding other offices The Director, including any individual serving as the Director in an acting capacity, may not hold another office or position in the Government of the United States while serving as the Director. (4) Absence or unavailability of Director Notwithstanding any provision of subchapter III of chapter 33, if the Director dies, resigns, or is otherwise unable to perform the function and duties of the office, the most senior career individual serving in the office of the Chief of Staff of the Office of Government Ethics, as of the date of the death, resignation, or beginning of inability to serve, shall serve as the Director until an individual is appointed by the President as the Director in accordance with this subsection. .\nC\nRestoring accountability and services\n#### 211. Report on effects of removing essential programs, offices, and services from Department of Veterans Affairs\n##### (a) Report required\nNot later than 30 days after the date of the enactment of this Act, the Secretary shall submit to Congress a report on the effects of removing essential programs, offices, and services from the Department of Veterans Affairs during the period beginning on January 20, 2025, and ending on the date of the enactment of this Act.\n##### (b) Contents\nThe report submitted pursuant to subsection (a) shall include, for the period covered by the report, the following:\n**(1)**\nA description of all offices or programs either reorganized, renamed, shut down, or reduced.\n**(2)**\nPosition titles of individuals either terminated or placed on leave, disaggregated by which office they were housed in.\n**(3)**\nA list of all websites, pamphlets, fliers, reports, photographs, or other public-facing documents removed.\n**(4)**\nA detailed description of how accessibility of Department facilities and websites has been affected, for both veterans and Department employees.\n**(5)**\nA list of any Department research projects cancelled or postponed.\n**(6)**\nA list of all Department employee-facing documents or trainings removed from intranet sites.\n**(7)**\nA list of all events cancelled or postponed by the Department.\n**(8)**\nFor each of paragraphs (1) through (7), a justification for why each action was taken.\n#### 212. Restoring Department of Veterans Affairs programs, offices, and services affected since the beginning of the second Trump Administration\n##### (a) Restoring Department of Veterans Affairs\n**(1) In general**\nAny removal, demotion, or suspension of a Department of Veterans Affairs employee during the period beginning on January 20, 2025, and ending on the date of the enactment of this Act shall be considered null and void.\n**(2) Backpay and resumption of benefits**\nA person subject to a removal, demotion, or suspension described in paragraph (1) shall be eligible for backpay and resumption of benefits.\n**(3) Resignations**\nA person described in paragraph (2) who does not wish to be restored to a position from which the person was removed, demoted, or suspended as described in paragraph (1) may resign from the position as they so choose.\n##### (b) Publication of certain materials and websites\nThe Secretary of Veterans Affairs shall commence publishing all materials and websites described in section 211(b).\n##### (c) Nullification of cancellation or postponement of certain research projects\nThe cancellation or postponement of any research projects during the period beginning on January 20, 2025, and ending on the date of the enactment of this Act shall be considered null and void.\n##### (d) Withdrawal of certain directive relating to flags\nThe Secretary shall withdraw the February 12, 2025 directive of the Secretary entitled Public Display or Depiction of Flags throughout Department of Veterans Affairs (VA) Facilities .\nIII\nProtections for civil servants\n#### 301. Nominations to Merit Systems Protection Board\nSubchapter I of chapter 12 of title 5, United States Code, is amended in section 1202, by adding at the end the following:\n(e) Not later than 30 days after the date on which a vacancy on the Merit Systems Protection Board occurs (whether before or at the end of a term of office of a member), the President shall appoint an individual to fill that vacancy. .\n#### 302. Modifications to appeal rights for probationary employees\nSection 7701(a) of title 5, United States Code, is amended, in the matter preceding paragraph (1), by inserting (including, notwithstanding any other provision of law, an employee who is in a probationary period) .\n#### 303. Authority to retract offers and contracts relating to deferred resignations\n##### (a) Authority\nAny offer or contract relating to deferred resignation commitment accepted or entered into by an employee in a position in the civil service may be nullified by the employee (without penalty) at any time until the close of business on the last day of the employment of the employee by the agency employing the employee.\n##### (b) Remedy\nA violation of subsection (a) may be appealed to the Merit Systems Protection Board in accordance with the procedures under section 7701 of title 5, United States Code, or challenged in a court of competent jurisdiction.\n#### 304. Limitation on changes to competitive service categories of positions\n##### (a) Limitation\nA position in the civil service may not be shifted, realigned, or removed from a competitive service category to an excepted service category\u2014\n**(1)**\nunless\u2014\n**(A)**\nthe employee who current fills the position agrees to such a shift; or\n**(B)**\nthe position is vacant; or\n**(2)**\nuntil the date that is 2 years after the date on which the head of the agency employing the employee has given notice to the employee and submitted to Congress notice of such a shift, realignment, or removal.\n##### (b) Remedy\nA violation of subsection (a) may be appealed to the Merit Systems Protection Board in accordance with the procedures under section 7701 of title 5, United States Code, or reviewed by a court of competent jurisdiction.\nIV\nMental health care for civil servants\n#### 401. Mental health services\nThe agency that currently employs, or most recently employed, a veteran, military spouse, caregiver, survivor, or member of a reserve component serving in a position in the civil service who is removed, demoted, or suspended on or after January 20, 2025, shall reimburse the veteran, military spouse, caregiver, survivor, or member of a reserve component for the cost of all mental health services provided during the 90-day period beginning on the date of the removal, demotion, or suspension.\n#### 402. Mental health services for current civil servants\n##### (a) Vet Centers\nThe Secretary of Veterans Affairs shall deploy a mobile Vet Center to the office of any agency that, on or after January 20, 2025, removes, suspends, or demotes a group of more than 5 veterans, military spouses, caregivers, survivors, or members of a reserve component on any day, for use by any current or former employees of the agency who are a veteran, military spouse, caregiver, survivor, or member of a reserve component.\n##### (b) Funding\nSubject to the availability of appropriations, until February 1, 2030, an agency may not reduce the amount of funds spent, contracts, staff, or programming related to mental health counseling services, financial and legal services, dependent care services, workplace conflict resolution services, cultural competency services, substance use treatment services, crisis intervention services, or employee assistance programs below the levels as of January 5, 2025.\nV\nEmployment assistance for civil servants\n#### 501. Employment assistance\nThe President shall order measures to provide employment assistance and opportunities for veterans, military spouses, caregivers, survivors, and members of a reserve component who are removed, demoted, or suspended from civil service on or after January 20, 2025.\n#### 502. Office of Personnel Management and the Department of Labor work on employment opportunities for members of the military community\nThe Director of the Office of Personnel Management and the Secretary of Labor shall\u2014\n**(1)**\nwork with the heads of other agencies to expand and facilitate the use of Federal programs, hiring and training opportunities, and retention incentives for veterans, military spouses, caregivers, survivors, and members of a reserve component;\n**(2)**\nseek to develop partnerships with firms in the private sector to enhance employment opportunities for veterans, military spouses, caregivers, survivors, and members of a reserve component, including to provide for improved job portability for such individuals;\n**(3)**\nwork with the United States Chamber of Commerce and other appropriate private-sector entities to facilitate the formation of such partnerships; and\n**(4)**\nexamine and seek ways for incorporating hiring preferences for veterans, military spouses, caregivers, survivors, and members of a reserve component into contracts between an agency and 1 or more private sector entities.\nVI\nDepartment of Government Efficiency\n#### 601. Limitation on access to veteran and department information, systems, and data\n##### (a) Limitations\n**(1) In general**\nSubchapter III of chapter 57 of title 38, United States Code, is amended by adding at the end of the following new section:\n5729. Limitations on access to certain information, systems, and data (a) In general The Secretary may not allow any individual to use, exercise administrative control over, or otherwise access any Department information technology system, health or benefits data repository, contracting information, financial system, record system, or other relevant system, or any data from any such system, unless\u2014 (1) such individual is an officer, employee, or contractor of the Department; and (2) in the case of an individual not described in paragraph (1)\u2014 (A) such individual holds a security clearance at the appropriate level with respect to such system or data and such clearance was granted pursuant to the procedures established under section 801 of the National Security Act of 1947 ( 50 U.S.C. 3161 ); (B) such individual\u2019s access to such system or data, or use thereof, does not constitute a violation of section 208 of title 18 (determined after the application of subsection (b)); (C) such individual is not a special Government employee (as defined in section 202 of title 18); (D) such individual\u2019s current continuous service in the civil service (as that term is defined in section 2101 of title 5) as of the date of such access is for a period of not less than one year; (E) such individual has completed any required training or compliance procedures with respect to privacy laws, cybersecurity regulations, national security regulations, and best practices; and (F) has signed a written ethics agreement with either the senior career Designated Agency Ethics Official of the Department, or the most senior career official within the Office of Government Ethics. (b) Treatment of individuals who are not officers or employees of executive branch of Federal Government (1) Any individual who accesses any system or data described in subsection (a) who is not otherwise an officer or employee of the executive branch of the Federal Government shall be treated as an employee of the executive branch of the United States Government for purposes of section 208 of title 18. (2) For purposes of such section 208, exercise of administrative control or stopping, canceling, adjusting, holding, rejecting, changing, or otherwise impacting any payment or data in any Department system, data repository, or other similar location, shall be considered personal and substantial participation as a Government officer or employee in a particular matter. (c) Definition of other relevant system In this section, the term other relevant system means any data, system, connection, database, repository, or any other tangible thing of the Department that stores information of the Department, veterans, surviving spouses, caregivers, or other recipients of health care or benefits under laws administered by the Secretary, including health data, personally identifiable information, protected health information, burial data information, contract data, the Corporate Data Warehouse of the Department, data regarding benefits provided to veterans, financial transaction and bank information, Department of Veterans Affairs Integrated Enterprise Workflow Solution system and data, payroll information, research and development data, and data that is part of the Million Veteran Program. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 57 of such title is amended by inserting after section 5728 the following new section:\n5729. Limitations on access to certain information, systems, and data. .\n##### (b) Deletion of improperly obtained data\nIn any action brought against the Department of Veterans Affairs or a recipient agency or other recipient in a court of competent jurisdiction for a violation of subsection (b) or (e) of section 552a of title 5, United States Code, the court may order the Secretary of Veterans Affairs, the recipient agency, or other recipient to delete records improperly disclosed or maintained in a system of records in violation of the rules and regulations set out pursuant to such section.\n##### (c) Removal of connections\nNot later than 15 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall remove any information technology connection between the Department and any entity not in compliance with the provisions of this section or section 5729 of title 38, United States Code, as added by subsection (a).\n#### 602. Limitation on application of certain Executive Orders relating to Department of Government Efficiency at Department of Veterans Affairs\nExecutive Order 14158 (90 Fed. Reg. 8441; relating to establishing and implementing the President\u2019s Department of Government Efficiency), Executive Order 14210 (90 Fed. Reg. 9669; relating to implementing the President\u2019s Department of Government Efficiency workforce optimization initiative), Executive Order 14219 (90 Fed. Reg. 10583; relating to ensuring lawful governance and implementing the President\u2019s Department of Government Efficiency deregulatory initiative), and Executive Order 14222 (90 Fed. Reg. 11095; relating to implementing the President\u2019s Department of Government Efficiency cost efficiency initiative) shall not apply as it relates to the Secretary of Veterans Affairs or the Department of Veterans Affairs.\n#### 603. Report on compliance with limitation on access to veteran and Department of Veterans Affairs information, systems, and data and Inspector General review\n##### (a) Report on compliance\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the compliance of the Department of Veterans Affairs with the provisions of this section and section 5729 of title 38, United States Code, as added by section 601(a), including with respect to removal of connections pursuant to section 601(c) and the removal of relevant employees and their credentials from all Department systems, premises, and networks consistent with the such sections.\n##### (b) Inspector General review\n**(1) Review**\nNot later than 10 days of after the date of the enactment of this Act, the Inspector General of the Department of Veterans Affairs shall initiate a review on any instance of unauthorized use or other access of systems described in section 5729(a) of title 38, United States Code, as added by section 601(a), that has occurred during the period beginning on November 6, 2024, and ending on the date of the enactment of this Act.\n**(2) Preliminary briefing**\nNot later than 90 days after the date of the enactment of this Act, the Inspector General shall provide the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a preliminary briefing on the findings of the Inspector General with respect to the review initiated pursuant to paragraph (1).\n**(3) Final report**\nNot later than 180 days after the date of the enactment of this Act, the Inspector General shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a final report on\u2014\n**(A)**\nthe findings of the Inspector General with respect to the review initiated pursuant to paragraph (1); and\n**(B)**\nsuch recommendations for administrative or legislative action as the Inspector General may have as a result of such findings.\n**(4) Contents**\nEach report submitted under this subsection shall include the following:\n**(A)**\na detailed description of the unauthorized use or access, including any actions the individual or individuals carried out;\n**(B)**\na risk assessment of any threat to privacy, contracting and financial information, protected veteran health and disability information, national security, cybersecurity, or the integrity of the applicable system as a result of such unauthorized use or access; and\n**(C)**\na detailed description of any stopped benefits, health care delivery, or other services of the Department of Veterans Affairs during the unauthorized use or access.\nVII\nFinancial needs of the Department of Veterans Affairs\n#### 701. Definition; rule of construction\n##### (a) Mass contract cancellation defined\nIn this title, the term mass contract cancellation means the termination by the Secretary of Veterans Affairs of\u2014\n**(1)**\nfive or more contracts in a single business day; or\n**(2)**\nten or more contracts in a five-business-day period.\n##### (b) Rule of construction\nNothing in this title shall be construed to prevent the Secretary of Veterans Affairs from cancelling individual contracts for poor performance, fraud, breach of contract, or other reasons in accordance with applicable law, including the Federal Acquisition Regulation.\n#### 702. Report on financial effect of the Department of Government Efficiency on the Department of Veterans Affairs\n##### (a) In general\nNot less frequently than once each quarter until September 30, 2029, the Secretary of Veteran Affairs shall submit to the appropriate committees of Congress a report detailing the estimated costs associated with or attributed to policy changes prompted by the Department of Government Efficiency or the President since January 20, 2025.\n##### (b) Costs\nEach report required by subsection (a) shall account for the following:\n**(1)**\nThe cancellation of any contracts and potential litigation to resolve related matters.\n**(2)**\nThe wrongful termination of employees and any settlements.\n**(3)**\nThe need to hire contracted providers or staff to backfill vacant roles.\n**(4)**\nSuch other matters as the Secretary of Veterans Affairs considers appropriate.\n##### (c) Appropriate committees of Congress defined\nIn this section, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the Senate; and\n**(2)**\nthe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the House of Representatives.\n#### 703. Reinstatement of contracts and review of mass contract cancellations\n##### (a) Reinstatement; pause; review\n**(1) In general**\nThe Secretary of Veterans Affairs\u2014\n**(A)**\nshall reinstate each contract cancelled in a mass contract cancellation during the period beginning on January 20, 2025, and ending on the date of the enactment of this Act;\n**(B)**\nshall pause any mass contract cancellation in progress as of the date of the enactment of this Act; and\n**(C)**\nshall not commence any mass contract cancellation unless\u2014\n**(i)**\neach condition described in paragraph (2) is met; and\n**(ii)**\nthe requirements of section 704 are fulfilled.\n**(2) Conditions**\nThe conditions described in this paragraph are the following:\n**(A)**\nThe Secretary of Veterans Affairs has reviewed all contracts cancelled or proposed to be cancelled during the period beginning on January 20, 2025 and ending on April 30, 2025.\n**(B)**\nThe Secretary has submitted to Congress a report on the reviews conducted under subparagraph (A), including, for each contract reviewed, a certification by the Secretary and career head of each relevant administration or office of the Department of Veterans Affairs that canceling the contract has not or will not affect any of the following:\n**(i)**\nThe delivery of health care, benefits, and memorial services to veterans.\n**(ii)**\nSafety and cleanliness of any facility of the Department, including surgical suites.\n**(iii)**\nThe ability of the Department to prevent and detect waste, fraud, and abuse.\n**(iv)**\nMedical research carried out by the Department.\n**(v)**\nCyber and information security.\n**(vi)**\nPlanning, delivery, and maintenance for infrastructure, leasing, and construction.\n**(vii)**\nHomelessness services, including prevention and housing.\n**(viii)**\nCancer research and care.\n**(ix)**\nMemorial services.\n**(x)**\nClaims processing and retrieval and digitization of records.\n**(xi)**\nVeteran-directed care.\n**(xii)**\nPayments and program oversight for educational assistance under laws administered by the Secretary of Veterans Affairs.\n**(xiii)**\nMedical supplies.\n**(xiv)**\nMental health and suicide prevention.\n**(xv)**\nImplementation of the Sergeant First Class Heath Robinson Honoring our Promise to Address Comprehensive Toxics Act of 2022 ( Public Law 117\u2013168 ) (commonly known as the PACT Act ).\n**(xvi)**\nRadiology services.\n**(xvii)**\nPharmacy services.\n**(xviii)**\nProsthetics services.\n**(xix)**\nThe Transition Assistance Program.\n**(xx)**\nThe Home Loan Guaranty Program of the Department.\n**(xxi)**\nPolice and security services provided by the Department.\n**(xxii)**\nEmergency response, including the Fourth Mission of the Department.\n**(xxiii)**\nVeterans employment.\n**(xxiv)**\nThe disposal of waste, including hazardous waste.\n**(xxv)**\nAny other critical service, function, or operation of the Department, including those required by statute.\n**(C)**\nThe Secretary has submitted to Congress a report that sets forth a day-by-day timeline of how the effort to carry out mass contract cancellations was initiated, led, and unfolded, including the following:\n**(i)**\nAn identification of each of the following:\n**(I)**\nWho directed the effort to begin and the date on which such direction took place.\n**(II)**\nThe parameters of the effort.\n**(III)**\nWhether the Department was provided with a dollar number target to meet for savings or whether officials of the Department determined the amount of savings desired.\n**(IV)**\nThe search terms used to select contracts for cancellation.\n**(V)**\nWho led the contract review process.\n**(VI)**\nThe specific individuals who reviewed the justifications to defend the merits of each contract.\n**(VII)**\nThe data and fact-based criteria used to decide which contracts should be cancelled based on the review of the defense of those contracts prepared by career officials.\n**(VIII)**\nWhether any contracts were removed from the initial list of contracts to be cancelled prior to that list being finalized.\n**(IX)**\nThe criteria used to develop the list of contracts announced for termination on March 3, 2025.\n**(ii)**\nAn estimate developed by the Chief Financial Officer or the Assistant Secretary for Management of the Department of the cost expended by employees of the Department to respond to data calls and contract justification exercises during the period beginning on January 20, 2025 and ending on April 30, 2025.\n**(iii)**\nA list of contracts cancelled during the period described in clause (ii) that were subsequently restored, and any costs paid by the Department to the contractor to mitigate the temporary cancellation, including legal fees.\n**(iv)**\nFor each contract that was cancelled, an estimated cost for the work to be performed by government personnel and an identification of the part of the Department those personnel will come from considering the ongoing partial hiring freeze and reduction in force efforts of the Department, including those outlined in the Departmental memorandum dated March 4, 2025, and entitled Department of Veterans Affairs Agency Reduction in Force (RIF) and Reorganization Plan (ARRP) .\n##### (b) Inspector General review\nNot later than one year after the date on which the reports required by subsection (a) are submitted to Congress, the Inspector General of the Department shall\u2014\n**(1)**\nreview the reports for accuracy and completeness; and\n**(2)**\nsubmit to Congress and make publicly available a report that includes\u2014\n**(A)**\nfindings regarding whether the process for mass contract cancellations was consistent with public statements of Department officials;\n**(B)**\nrecommendations for areas for improvement for future contract management and oversight; and\n**(C)**\nsuch other matters as the Inspector General considers appropriate, including actions the Department may take to improve oversight and use of Federal resources in order to improve efficiency in contracting by the Department and prevent and detect waste, fraud, and abuse.\n#### 704. Limitations on mass contract cancellations\n##### (a) Submission required\n**(1) In general**\nAfter the conditions described in section 703(a)(2) are met, if the Secretary of Veterans Affairs decides to carry out a mass contract cancellation, the Secretary shall, before carrying out such cancellation, submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives the following:\n**(A)**\nA list of contracts proposed for cancellation.\n**(B)**\nFor each contract included in the list described in subparagraph (A), a certification described in section 703(a)(2)(B).\n**(C)**\nThe number of contracts included in such list that are held by a service-disabled veteran-owned small business or a veteran-owned small business.\n**(D)**\nA description of how the work proposed to be cancelled would be absorbed by the existing workforce of the Department or whether hiring of additional staff will be needed to perform that work, and a cost benefit analysis comparing the contracting and staffing approaches.\n**(2) Limitation**\nThe Secretary of Veterans Affairs shall not commence a mass contract cancellation until the date that is 30 days after the date on which the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives receive the submission for such cancellation under paragraph (1).\n##### (b) Report\n**(1) In general**\nNot later than 7 business days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report that includes the following:\n**(A)**\nA list of the contracts cancelled or proposed for cancellation developed by the Department and announced by the Secretary of Veterans Affairs on February 25, 2025, and, for each contract included in such list\u2014\n**(i)**\nthe justification for the need for the contract, if submitted, as written by career employees of the Department; and\n**(ii)**\nan indication of whether the entity holding the contract is a service-disabled veteran-owned small business or a veteran-owned small business.\n**(B)**\nA list of contracts announced for cancellation by the Department of Veterans Affairs on March 3, 2025, and, for each contract included in such list\u2014\n**(i)**\nthe justification for the need for the contract, if submitted, as written by career employees of the Department; and\n**(ii)**\nan indication of whether the entity holding the contract is a service-disabled veteran-owned small business or a veteran-owned small business.\n**(2) Data fields**\nEach list described in paragraph (1) shall contain, at a minimum, the following fields:\n**(A)**\nContract/Order #/PIID.\n**(B)**\nVendor.\n**(C)**\nCategory of contract using relevant North American Industry Classification System (NAICS) terminology.\n**(D)**\nContract description.\n**(E)**\nDate of termination or contract action.\n**(F)**\nContracting Unique Entity Identifier.\n**(G)**\nThe headquarters city and State of the vendor.\n#### 705. Charge card program of the Department of Veterans Affairs\n##### (a) In general\nNot later than 60 days before making any change to the charge card program of the Department of Veterans Affairs, including any change reducing the total number of charge cards authorized for use, the Secretary of Veterans Affairs shall notify the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives in writing of the proposed change.\n##### (b) Elements\nAny notification required by subsection (a) shall include the following:\n**(1)**\nThe justification for the change concerned.\n**(2)**\nThe timeline for the change to occur.\n**(3)**\nA description of how the Secretary of Veterans Affairs intends to monitor for any negative effects on health care or benefits delivery.\n##### (c) Sunset\nThis section shall terminate on the date on which President Trump is no longer President.\nVIII\nReporting requirements\n#### 801. Requirement for Veterans Benefits Administration Monday Morning Workload Report\n##### (a) In general\nChapter 53 of title 38, United States Code, is amended by adding at the end the following new section:\n5322. Monday Morning Workload Report (a) In general Not less frequently than once each week, the Under Secretary for Benefits shall publish on a publicly available website of the Department, a report providing a snapshot of the workload of the Veterans Benefits Administration. (b) Contents Each report published pursuant to subsection (a) shall include the following: (1) National totals for pending and backlogged compensation, pension, appeals, and education workloads of the Veterans Benefits Administration. (2) National, district, and regional office-level data, disaggregated by the following: (A) Station of jurisdiction. (B) Station of origination. (C) State. (D) National Work Queue, or successor queue, including\u2014 (i) the number of claims pending at stage of the claims life cycle; and (ii) average time claims are pending at each stage of a life cycle. (3) Data for groups of claims, disaggregated by national, district, and regional office or State level, including non-rating bundle, entitlement bundle, award adjustments bundle, program review bundle, other bundle, burial claims, accrued claims, appeals, number of claims and appeals with duty to assist errors, and such other groups as the Secretary considers appropriate. (4) National level data on claim and appeal inventories, disaggregated by end product code. (5) Regional office level data on claim and appeal inventories, disaggregated by traditional aggregate groups. (6) National level data on the future volume of work of which the Under Secretary is aware. (7) Average age of claims that have maintained continuous pursuit. (8) Factors contributing to the increase or decrease in workload and the claims backlog. (9) Such additional data as the Under Secretary considers appropriate. (c) Publication requirement Each report published pursuant to subsection (a) in a week shall be published on the Monday of that week, except as follows: (1) In a case in which the Monday of the week of publication is a Federally recognized holiday, the report shall be published on the Tuesday of that week. (2) In a case in which the Secretary is publishing the report required by subsection (a) more than once in a single week, any publication after the first publication may be made on any day of the week at the discretion of the Under Secretary. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 53 of such title is amended by adding after the item relating to section 5321 the following new item:\n5322. Monday Morning Workload Report. .\n#### 802. Improvements regarding periodic publication of metrics relating to processing of appeals\nSection 5 of the Veterans Appeals Improvement and Modernization Act of 2017 ( Public Law 115\u201355 ) is amended by adding at the end the following new paragraph:\n(4) A summary of the outcome of appeals under the new appeals system, including appeals reviewed by the Board of Veterans\u2019 Appeals, disaggregated by\u2014 (A) the type of review; (B) station of origination; (C) type of appeal; and (D) diagnostic codes. .\n#### 803. Publication of wait times for community care from Department of Veterans Affairs\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall publish on a publicly accessible website of each medical center of the Department of Veterans Affairs the wait times for scheduling an appointment for a veteran to receive care from a non-Department provider in the community for that medical center and each of the clinics of the Department in the catchment area of that medical center.\n##### (b) Data To be included\nThe Secretary shall include in the publication under subsection (a) wait times for the following care:\n**(1)**\nPrimary care.\n**(2)**\nSpecialty care.\n**(3)**\nInpatient care.\n**(4)**\nMental health care.\n**(5)**\nSuch other types of care as the Secretary considers appropriate.\n##### (c) Update\nThe Secretary shall update the wait times published under subsection (a) not less frequently than weekly.\n##### (d) Metrics used\nThe Secretary shall calculate the wait times published under subsection (a) based on similar metrics as the metrics used to calculate wait times for care at facilities of the Department.\n#### 804. Period for Secretary of Veterans Affairs to respond to questions submitted by members of certain congressional committees\n##### (a) Requirement\nTo the maximum extent practicable, the Secretary of Veterans Affairs shall provide\u2014\n**(1)**\nan answer to a question submitted for the record to the Department of Veterans Affairs by a member of the Committee on Veterans\u2019 Affairs of the Senate or the Committee on Veterans\u2019 Affairs of the House of Representatives, on or before the date that is 45 business days after the date on which the Department receives the question;\n**(2)**\nan answer to a request for information submitted by a member of the staff of the Committee on Veterans\u2019 Affairs of the Senate or the Committee on Veterans\u2019 Affairs of the House of Representatives or a member of either committee, on or before the date that is 15 business days after the date on which the Department receives the request from the member of the staff or the member of the committee, as the case may be; and\n**(3)**\nan answer to a letter sent by a member of the Committee on Veterans\u2019 Affairs of the Senate or the Committee on Veterans\u2019 Affairs of the House of Representatives, on or before the date that is 15 business days after the date on which the Department receives the letter.\n##### (b) Delayed responses\n**(1) Notice required**\nIf the Secretary anticipates being unable to provide an answer to a question, request for information, or letter described in subsection (a) that was submitted to the Department by the date specified in such subsection, the Secretary shall, before such date, submit to the member and the relevant Committee a notice that the Secretary anticipates being unable to provide the answer by such date.\n**(2) Contents**\nNotice submitted under paragraph (1) shall include the following:\n**(A)**\nA justification for the inability of the Secretary to meet the deadline set forth in subsection (a).\n**(B)**\nAn estimate of when an answer will be provided by the Secretary to the question, request for information, or letter submitted.\n**(C)**\nA description of the steps the Secretary needs to take in order to provide the response, including steps required to obtain any information required of another Federal agency.",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T13:52:59Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1068is.xml"
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
      "title": "Putting Veterans First Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Putting Veterans First Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5 and title 38, United States Code, to put veteran and military families first and to provide protections for employees, benefits, and programs of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:18:36Z"
    }
  ]
}
```
