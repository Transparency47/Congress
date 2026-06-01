# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/928?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/928
- Title: Railway Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 928
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-03-05T09:06:45Z
- Update date including text: 2026-03-05T09:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-04 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-04 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/928",
    "number": "928",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Railway Safety Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-05T09:06:45Z",
    "updateDateIncludingText": "2026-03-05T09:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-02-04T17:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-04T22:12:47Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-04T17:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
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
      "sponsorshipDate": "2025-03-14",
      "state": "PA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MD"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NY"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "DC"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "PA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr928ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 928\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Deluzio (for himself, Mr. LaLota , Mr. Rulli , and Mr. Garamendi ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo enhance safety requirements for trains transporting hazardous materials, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Railway Safety Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Defined term.\nSec. 3. Safety requirements for trains transporting hazardous materials.\nSec. 4. Rail car inspections.\nSec. 5. Defect detectors.\nSec. 6. Safe Freight Act of 2025.\nSec. 7. Increasing maximum civil penalties for violations of rail safety regulations.\nSec. 8. Safer tank cars.\nSec. 9. Hazardous materials training for first responders.\nSec. 10. Consolidated rail infrastructure and safety improvements.\nSec. 11. Tank car study.\nSec. 12. Implementation of recommendations.\n#### 2. Defined term\nIn this Act, the term Secretary means the Secretary of Transportation.\n#### 3. Safety requirements for trains transporting hazardous materials\n##### (a) Rulemaking\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall issue regulations, or modify existing regulations, establishing safety requirements, in accordance with subsection (b), with which a shipper or rail carrier operating a train transporting hazardous materials that is not subject to the requirements for a high-hazard flammable train under section 174.310 of title 49, Code of Federal Regulations, shall comply with respect to the operation of each such train and the maintenance of specification tank cars.\n##### (b) Requirements\nThe regulations issued pursuant to subsection (a) shall require shippers and rail carriers\u2014\n**(1)**\nto provide advance notification and information regarding the transportation of hazardous materials described in subsection (a) to each State emergency response commissioner, Tribal emergency response commission, or any other State or Tribal agency responsible for receiving the information notification for emergency response planning information;\n**(2)**\nto include, in the notification provided pursuant to paragraph (1), a written gas discharge plan with respect to the applicable hazardous materials being transported; and\n**(3)**\nto reduce or eliminate blocked crossings resulting from delays in train movements.\n##### (c) Additional requirements\nIn developing the regulations required under subsection (a), the Secretary shall include requirements regarding\u2014\n**(1)**\ntrain length and weight;\n**(2)**\ntrain consist;\n**(3)**\nroute analysis and selection;\n**(4)**\nspeed restrictions;\n**(5)**\ntrack standards;\n**(6)**\ntrack, bridge, and rail car maintenance;\n**(7)**\nsignaling and train control;\n**(8)**\nresponse plans; and\n**(9)**\nany other requirements that the Secretary determines are necessary.\n##### (d) High-Hazard flammable trains\nThe Secretary may modify the safety requirements for trains subject to section 174.310 of title 49, Code of Federal Regulations, to satisfy, in whole or in part, the rulemaking required under subsection (a).\n#### 4. Rail car inspections\n##### (a) Rulemaking\n**(1) Inspection requirements**\nNot later than 1 year after date of the enactment of this Act, the Secretary shall review and update, as necessary, applicable regulations under chapters I and II of subtitle B of title 49, Code of Federal Regulations\u2014\n**(A)**\nto create minimum time requirements that a qualified mechanical inspector must spend when inspecting a rail car or locomotive; and\n**(B)**\nto ensure that all rail cars and locomotives in train consists that carry hazardous materials are inspected by a qualified mechanical inspector at intervals determined by the Secretary.\n**(2) Abbreviated pre-departure inspection**\nThe Secretary shall immediately amend section 215.13(c) of title 49, Code of Federal Regulations (permitting an abbreviated pre-departure inspection procedure) with respect to rail cars in train consists carrying hazardous materials.\n##### (b) Audits\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary shall initiate audits of Federal rail car inspection programs, subject to the requirements under part 215 of title 49, Code of Federal Regulations, which\u2014\n**(A)**\nconsider whether such programs are in compliance with such part 215;\n**(B)**\nassess the type and content of training and performance metrics that such programs provide rail car inspectors;\n**(C)**\ndetermine whether such programs provide inspectors with adequate time to inspect rail cars;\n**(D)**\ndetermine whether such programs reflect the current operating practices of the railroad carrier; and\n**(E)**\nensure that such programs are not overly reliant on train crews.\n**(2) Audit scheduling**\nThe Secretary shall\u2014\n**(A)**\nschedule the audits required under paragraph (1) to ensure that\u2014\n**(i)**\neach Class I railroad is audited not less frequently than once every 5 years; and\n**(ii)**\na select number, as determined by the Secretary, of Class II and Class III railroads are audited annually; and\n**(B)**\nconduct the audits described in subparagraph (A)(ii) in accordance with\u2014\n**(i)**\nthe Small Business Regulatory Enforcement Fairness Act of 1996 ( 5 U.S.C. 601 note); and\n**(ii)**\nappendix C of part 209 of title 49, Code of Federal Regulations.\n**(3) Updates to inspection program**\nIf, during an audit required under this subsection, the auditor identifies a deficiency in a railroad's inspection program, the railroad shall update the program to eliminate such deficiency.\n**(4) Consultation and cooperation**\n**(A) Consultation**\nIn conducting any audit required under this subsection, the Secretary shall consult with the railroad being audited and its employees, including any nonprofit employee labor organization representing the mechanical employees of the railroad.\n**(B) Cooperation**\nThe railroad being audited and its employees, including any nonprofit employee labor organization representing mechanical employees, shall fully cooperate with any audit conducted pursuant to this subsection\u2014\n**(i)**\nby providing any relevant documents requested; and\n**(ii)**\nby making available any employees for interview without undue delay or obstruction.\n**(C) Failure to cooperate**\nIf the Secretary determines that a railroad or any of its employees, including any nonprofit employee labor organization representing mechanical employees of the railroad is not fully cooperating with an audit conducted pursuant to this subsection, the Secretary shall electronically notify the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives of such noncooperation.\n##### (c) Review of regulations\nThe Secretary shall triennially determine whether any update to part 215 of title 49, Code of Federal Regulations, is necessary to ensure the safety of rail cars transported by rail carriers.\n##### (d) Annual report\nThe Secretary shall publish an annual report on the public website of the Federal Railroad Administration that\u2014\n**(1)**\nsummarizes the findings of the prior year's audits;\n**(2)**\nsummarizes any updates made pursuant to this section; and\n**(3)**\nexcludes any confidential business information or sensitive security information.\n##### (e) Rule of construction\nNothing in this section may be construed\u2014\n**(1)**\nto limit the deployment of pilot programs for the installation, test, verification, and review of automated rail and train inspection technologies; or\n**(2)**\nto direct the Secretary to waive any existing inspection requirements under chapter I or II of subtitle B of title 49, Code of Federal Regulations, as part of pilot programs.\n#### 5. Defect detectors\n##### (a) Rulemaking\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall issue regulations establishing requirements for the installation, repair, testing, maintenance, and operation of wayside defect detectors for each rail carrier operating a train consist carrying hazardous materials.\n##### (b) Requirements\nThe regulations issued pursuant to subsection (a) shall include requirements regarding\u2014\n**(1)**\nthe frequency of the placement of wayside defect detectors, including a requirement that all Class I railroads install a hotbox detector along every 10-mile segment of rail track over which trains carrying hazardous materials operate;\n**(2)**\nperformance standards for such detectors;\n**(3)**\nthe maintenance and repair requirements for such detectors;\n**(4)**\nreporting data and maintenance records of such detectors;\n**(5)**\nappropriate steps the rail carrier must take when receiving an alert of a defect or failure from or regarding a wayside defect detector; and\n**(6)**\nthe use of hotbox detectors to prevent derailments from wheel bearing failures, including\u2014\n**(A)**\nthe temperatures, to be specified by the Secretary, at which an alert from a hotbox detector is triggered to warn of a potential wheel bearing failure; and\n**(B)**\nany actions that shall be taken by a rail carrier upon receiving an alert from a hotbox detector of a potential wheel bearing failure.\n##### (c) Defect and failure identification\nThe Secretary shall specify the categories of defects and failures that wayside defect detectors covered by regulations issued pursuant to subsection (a) shall address, including\u2014\n**(1)**\naxles;\n**(2)**\nwheel bearings;\n**(3)**\nbrakes;\n**(4)**\nsignals;\n**(5)**\nwheel impacts; and\n**(6)**\nother defects or failures specified by the Secretary.\n#### 6. Safe Freight Act of 2025\n##### (a) Short title\nThis section may be cited as the Safe Freight Act of 2025 .\n##### (b) Freight train crew size\nSubchapter II of chapter 201 of title 49, United States Code, is amended by inserting after section 20153 the following:\n20154. Freight train crew size safety standards (a) Minimum crew size No freight train may be operated without a 2-person crew consisting of at least 1 appropriately qualified and certified conductor and 1 appropriately qualified and certified locomotive engineer. (b) Exceptions Except as provided in subsection (c), the requirement under subsection (a) shall not apply with respect to\u2014 (1) train operations on track that is not a main line track; (2) a freight train operated\u2014 (A) by a railroad carrier that has fewer than 400,000 total employee work hours annually and less than $40,000,000 annual revenue (adjusted for inflation, as calculated by the Surface Transportation Board Railroad Inflation- Adjusted Index and Deflator Factor Table); (B) at a speed of not more than 25 miles per hour; and (C) on a track with an average track grade of less than 2 percent for any segment of track that is at least 2 continuous miles; (3) locomotives performing assistance to a train that has incurred mechanical failure or lacks the power to traverse difficult terrain, including traveling to or from the location where assistance is provided; (4) locomotives that\u2014 (A) are not attached to any equipment or are attached only to a caboose; and (B) do not travel farther than 30 miles from the point of origin of such locomotive; and (5) train operations staffed with fewer than a 2-person crew at least 1 year before the date of enactment of this section, if the Secretary determines that such operations achieve an equivalent level of safety as would result from compliance with the requirement under subsection (a). (c) Trains ineligible for exception The exceptions under subsection (b) may not be applied to\u2014 (1) a train transporting 1 or more loaded cars carrying material toxic by inhalation (as defined in section 171.8 of title 49, Code of Federal Regulations); (2) a train transporting\u2014 (A) 20 or more loaded tank cars of a Class 2 material or a Class 3 flammable liquid in a continuous block; or (B) 35 or more loaded tank cars of a Class 2 material or a Class 3 flammable liquid throughout the train consist; or (3) a train with a total length of at least 7,500 feet. (d) Waiver A railroad carrier may seek a waiver of the requirements under this section in accordance with section 20103(d). .\n##### (c) Clerical amendment\nThe analysis for subchapter II of chapter 201 of title 49, United States Code, is amended by inserting after the item relating to section 20153 the following:\n20154. Freight train crew size safety standards. .\n#### 7. Increasing maximum civil penalties for violations of rail safety regulations\n##### (a) Civil penalties related to transporting hazardous materials\nSection 5123(a) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), in the matter preceding subparagraph (A), by striking $75,000 and inserting the greater of 0.5 percent of the person\u2019s annual income or annual operating income, as applicable, or $750,000 ; and\n**(2)**\nin paragraph (2), by striking $175,000 and inserting the greater of 1 percent of the person\u2019s annual income or annual operating income, as applicable, or $1,750,000 .\n##### (b) General violations of chapter 201\nSection 21301(a)(2) of title 49, United States Code, is amended\u2014\n**(1)**\nby striking $25,000 and inserting the greater of 0.5 percent of the person\u2019s annual income or annual operating income, as applicable, or $250,000 ; and\n**(2)**\nby striking $100,000 and inserting the greater of 1 percent of the person\u2019s annual income or annual operating income, as applicable, or $1,000,000 .\n##### (c) Accident and incident violations of chapter 201; violations of chapters 203 through 209\nSection 21302(a) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking 203\u2013209 each place it appears and inserting 203 through 209 ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking $25,000 and inserting the greater of 0.5 percent of the person\u2019s annual income or annual operating income, as applicable, or $250,000 ; and\n**(B)**\nby striking $100,000 and inserting the greater of 1 percent of the person\u2019s annual income or annual operating income, as applicable, or $1,000,000 .\n##### (d) Violations of chapter 211\nSection 21303(a)(2) of title 49, United States Code, is amended\u2014\n**(1)**\nby striking $25,000 and inserting the greater of 0.5 percent of the person\u2019s annual income or annual operating income, as applicable, or $250,000 ; and\n**(2)**\nby striking $100,000 and inserting the greater of 1 percent of the person\u2019s annual income or annual operating income, as applicable, or $1,000,000 .\n#### 8. Safer tank cars\n##### (a) Phase-Out schedule\nNotwithstanding section 7304 of the FAST Act ( 49 U.S.C. 20155 note), beginning on May 1, 2027, a rail carrier may not use DOT\u2013111 specification railroad tank cars that do not comply with DOT\u2013117, DOT\u2013117P, or DOT\u2013117R specification requirements, as in effect on the date of enactment of this Act, to transport Class 3 flammable liquids regardless of the composition of the train consist.\n##### (b) Conforming regulatory amendments\n**(1) In general**\nThe Secretary\u2014\n**(A)**\nshall immediately remove or revise the date-specific deadlines in any applicable regulations or orders to the extent necessary to conform with the requirement under subsection (a); and\n**(B)**\nmay not enforce any date-specific deadlines or requirements that are inconsistent with the requirement under subsection (a).\n**(2) Rule of construction**\nExcept as required under paragraph (1), nothing in this section may be construed to require the Secretary to issue regulations to implement this section.\n#### 9. Hazardous materials training for first responders\n##### (a) Annual registration fee\nSection 5108(g) of title 49, United States Code, is amended by adding at the end the following:\n(4) Additional fee for class I rail carriers In addition to the fees collected pursuant to paragraphs (1) and (2), the Secretary shall establish and annually impose and collect from each Class I rail carrier a fee in an amount equal to $1,000,000. .\n##### (b) Assistance for local emergency response training\nSection 5116(j) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)(A), by striking liquids and inserting materials ; and\n**(2)**\nin paragraph (3), by amending subparagraph (A) to read as follows:\n(A) In general To carry out the grant program established pursuant to paragraph (1),the Secretary may expend, during each fiscal year\u2014 (i) the amounts collected pursuant to section 5108(g)(4); and (ii) any amounts recovered during such fiscal year from grants awarded under this section during a prior fiscal year. .\n##### (c) Supplemental training grants\nSection 5128(b)(4) of title 49, United States Code is amended by striking $2,000,000 and inserting $4,000,000 .\n#### 10. Consolidated rail infrastructure and safety improvements\n##### (a) In general\nSection 22907(c) of title 49, United States Code, is amended by adding at the end the following:\n(17) Expanding the use and effectiveness of wayside defect detectors to better prevent the derailment of trains transporting hazardous materials. .\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to carry out section 22907(c)(17) of title 49, United States Code (as added by subsection (a)), $22,000,000.\n#### 11. Tank car study\n##### (a) In general\nThe Administrator of the Pipeline and Hazardous Materials Safety Administration shall study, and submit to Congress a report on, technology available to develop\u2014\n**(1)**\nstronger, safer tank cars and valves for tank cars; and\n**(2)**\nother tank car safety features.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $5,000,000.\n#### 12. Implementation of recommendations\nNot later than 2 years after the date of enactment of this Act, and every 2 years thereafter, the Secretary of Transportation shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the progress of the Secretary in implementing the recommendations in chapter 4 of the report titled Norfolk Southern Railway Derailment and Hazardous Materials Release issued on June 25, 2024 by the National Transportation Safety Board (NTSB/RIR\u201324\u201305).",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-22T15:35:47Z"
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
          "measure-id": "id119hr928",
          "measure-number": "928",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-06-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr928v00",
            "update-date": "2025-06-18"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Railway Safety Act of 2025</strong></p><p>This bill addresses safety requirements for rail carriers and trains transporting hazardous materials.</p><p>Specifically, the Department of Transportation (DOT) must issue safety regulations for trains carrying hazardous materials to require that rail carriers or shippers (1) provide state emergency response commissioners with advance notice and information about the hazardous materials; (2) reduce blocked rail crossings; and (3) comply with certain requirements regarding train length and weight specifications, track standards, speed restrictions, and response plans.</p><p>DOT must also establish requirements for wayside defect detectors. These are used by railway systems alongside the tracks to detect defects and failures (e.g., wheel bearing failures). Current federal regulations do not require their use, but federal guidance does address their placement and use. Under the bill, DOT must issue regulations establishing requirements for the installation, repair, testing, maintenance, and operation of wayside defect detectors for each rail carrier operating a train carrying hazardous materials.</p><p>The bill also</p><ul><li>increases the maximum fines DOT may impose on rail carriers for violating safety regulations;</li><li>requires DOT to update rail car inspection regulations and audit the federal inspection programs;</li><li>establishes a statutory requirement\u00a0for freight trains to have at least two crew\u00a0members, with exceptions;</li><li>phases out certain railroad tank cars by May 1, 2027;</li><li>expands training for local first responders;</li><li>imposes a new fee on certain rail carriers; and</li><li>authorizes grants to improve railway safety.</li></ul>"
        },
        "title": "Railway Safety Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr928.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Railway Safety Act of 2025</strong></p><p>This bill addresses safety requirements for rail carriers and trains transporting hazardous materials.</p><p>Specifically, the Department of Transportation (DOT) must issue safety regulations for trains carrying hazardous materials to require that rail carriers or shippers (1) provide state emergency response commissioners with advance notice and information about the hazardous materials; (2) reduce blocked rail crossings; and (3) comply with certain requirements regarding train length and weight specifications, track standards, speed restrictions, and response plans.</p><p>DOT must also establish requirements for wayside defect detectors. These are used by railway systems alongside the tracks to detect defects and failures (e.g., wheel bearing failures). Current federal regulations do not require their use, but federal guidance does address their placement and use. Under the bill, DOT must issue regulations establishing requirements for the installation, repair, testing, maintenance, and operation of wayside defect detectors for each rail carrier operating a train carrying hazardous materials.</p><p>The bill also</p><ul><li>increases the maximum fines DOT may impose on rail carriers for violating safety regulations;</li><li>requires DOT to update rail car inspection regulations and audit the federal inspection programs;</li><li>establishes a statutory requirement\u00a0for freight trains to have at least two crew\u00a0members, with exceptions;</li><li>phases out certain railroad tank cars by May 1, 2027;</li><li>expands training for local first responders;</li><li>imposes a new fee on certain rail carriers; and</li><li>authorizes grants to improve railway safety.</li></ul>",
      "updateDate": "2025-06-18",
      "versionCode": "id119hr928"
    },
    "title": "Railway Safety Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Railway Safety Act of 2025</strong></p><p>This bill addresses safety requirements for rail carriers and trains transporting hazardous materials.</p><p>Specifically, the Department of Transportation (DOT) must issue safety regulations for trains carrying hazardous materials to require that rail carriers or shippers (1) provide state emergency response commissioners with advance notice and information about the hazardous materials; (2) reduce blocked rail crossings; and (3) comply with certain requirements regarding train length and weight specifications, track standards, speed restrictions, and response plans.</p><p>DOT must also establish requirements for wayside defect detectors. These are used by railway systems alongside the tracks to detect defects and failures (e.g., wheel bearing failures). Current federal regulations do not require their use, but federal guidance does address their placement and use. Under the bill, DOT must issue regulations establishing requirements for the installation, repair, testing, maintenance, and operation of wayside defect detectors for each rail carrier operating a train carrying hazardous materials.</p><p>The bill also</p><ul><li>increases the maximum fines DOT may impose on rail carriers for violating safety regulations;</li><li>requires DOT to update rail car inspection regulations and audit the federal inspection programs;</li><li>establishes a statutory requirement\u00a0for freight trains to have at least two crew\u00a0members, with exceptions;</li><li>phases out certain railroad tank cars by May 1, 2027;</li><li>expands training for local first responders;</li><li>imposes a new fee on certain rail carriers; and</li><li>authorizes grants to improve railway safety.</li></ul>",
      "updateDate": "2025-06-18",
      "versionCode": "id119hr928"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr928ih.xml"
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
      "title": "Railway Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Railway Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T04:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Freight Act of 2025",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-05-16T04:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance safety requirements for trains transporting hazardous materials, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T04:03:31Z"
    }
  ]
}
```
