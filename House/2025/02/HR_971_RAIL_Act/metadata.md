# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/971?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/971
- Title: RAIL Act
- Congress: 119
- Bill type: HR
- Bill number: 971
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-06-17T17:00:30Z
- Update date including text: 2025-06-17T17:00:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-04 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/971",
    "number": "971",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "RAIL Act",
    "type": "HR",
    "updateDate": "2025-06-17T17:00:30Z",
    "updateDateIncludingText": "2025-06-17T17:00:30Z"
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
          "date": "2025-02-04T17:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-04T22:13:07Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
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
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "OH"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr971ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 971\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mrs. Sykes (for herself, Mr. Rulli , Mrs. Beatty , Ms. Brown , Ms. Kaptur , and Mr. Landsman ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo enhance safety requirements for trains transporting hazardous materials, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Reducing Accidents In Locomotives Act or the RAIL Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Defined term.\nSec. 3. Recommendations for safety.\nSec. 4. Inspections.\nSec. 5. Defect detectors.\nSec. 6. Increasing maximum civil penalties for violations of rail safety regulations.\nSec. 7. Safer tank cars.\nSec. 8. Hazardous materials training for first responders.\nSec. 9. Freight train crew size safety standards.\n#### 2. Defined term\nIn this Act, the term Secretary means the Secretary of Transportation.\n#### 3. Recommendations for safety\n##### (a) Rulemaking\nNot later than 1 year after the date on which the National Transportation Safety Board issues the report on the East Palestine, Ohio crash, the Secretary, in consultation with the Administrator of the Federal Railroad Administration, shall issue regulations, or modify existing regulations, based on such report establishing safety requirements, in accordance with subsection (b), with which a rail carrier operating a train transporting hazardous materials that is not subject to the requirements for a high-hazard flammable train under section 174.310 of title 49, Code of Federal Regulations, shall comply with respect to the operation of each such train and the maintenance of specification tank cars.\n##### (b) Requirements\nThe regulations issued pursuant to subsection (a) shall require rail carriers\u2014\n**(1)**\nto provide advance notification and information regarding the transportation of hazardous materials described in subsection (a) to each State emergency response commissioner, the tribal emergency response commission, or any other State or tribal agency responsible for receiving the information notification for emergency response planning information;\n**(2)**\nto include, in the notification provided pursuant to paragraph (1), a written gas discharge plan with respect to the applicable hazardous materials being transported; and\n**(3)**\nto reduce or eliminate blocked crossings resulting from delays in train movements.\n##### (c) Additional requirements\nIn developing the regulations required under subsection (a), the Secretary shall include requirements regarding\u2014\n**(1)**\ntrain length and weight;\n**(2)**\ntrain consist;\n**(3)**\nroute analysis and selection;\n**(4)**\nspeed restrictions;\n**(5)**\ntrack standards;\n**(6)**\ntrack, bridge, and rail car maintenance;\n**(7)**\nsignaling and train control; and\n**(8)**\nresponse plans.\n#### 4. Inspections\n##### (a) Time available for inspection\n**(1) In general**\nSubchapter II of chapter 201 of title 49, United States Code, is amended by adding at the end the following:\n20172. Time available for inspection (a) In general No railroad may limit the time required for an employee to complete a railcar, locomotive, or brake inspection to ensure that each railcar, locomotive, and brake system complies with safety laws and regulations. (b) Requirement Employees shall perform their inspection duties promptly and shall not delay other than for reasons related to safety. .\n**(2) Clerical amendment**\nThe analysis for subchapter II of chapter 201 of title 49, United States Code, is amended by adding at the end the following:\n20172. Time available for inspection. .\n##### (b) Pre-Departure railcar inspections\nNot later than 120 days after the date of the enactment of this Act, the Secretary shall amend the pre-departure inspection requirements for Class I railroads under part 215 of title 49, Code of Federal Regulations (as written on such date of enactment)\u2014\n**(1)**\nto ensure that after initial consultation with the Federal Railroad Administration, and after each subsequent annual consultation, each railroad identifies inspection locations and, at such locations, has inspectors designated under part 215 available for the purpose of inspecting freight cars;\n**(2)**\nto ensure that all freight cars are inspected by an inspector designated under part 215 at a designated inspection location in the direction of travel as soon as practicable; and\n**(3)**\nto require each railroad that operates railroad freight cars to which such part 215 applies to designate persons qualified to inspect railroad freight rail cars, subject to any existing collective bargaining agreement, for compliance and determinations required under such part.\n##### (c) Qualified locomotive inspections\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall review and amend, as necessary, regulations under chapters 229 and 243 of title 49, Code of Federal Regulations\u2014\n**(1)**\nto ensure appropriate training qualifications and proficiency of employees, including qualified mechanical inspectors, performing locomotive inspections; and\n**(2)**\nfor locomotives in service on a Class I railroad, to require an additional daily inspection to be performed by a qualified mechanical inspector between the current intervals under section 229.23(b)(2) of title 49, Code of Federal Regulations.\n##### (d) Audits\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary shall initiate audits of Federal railcar, locomotive, and train brake system inspection compliance with chapter II of subtitle B of title 49, Code of Federal Regulations, which\u2014\n**(A)**\nconsider whether the railroad has in place procedures necessary for railcar, locomotive, and train brake system inspection compliance under such chapter;\n**(B)**\nassess the type, content, and adequacy of training and performance metrics the railroad provides employees who perform railcar, locomotive, and train brake system inspections, including the qualifications specified for such employees;\n**(C)**\ndetermine whether the railroad has practices that would interfere with an employee\u2019s responsibility to perform an inspection safely;\n**(D)**\ndetermine whether railcars, locomotives, and train brake systems are inspected on the railroad\u2019s network in accordance with such chapter;\n**(E)**\ninvolve proper communication of identified defects to railroad personnel and make appropriate use of remedial action reports to verify that repairs are made;\n**(F)**\ndetermine whether managers coerce employees to sign off on any documents verifying an inspection or repair of a railcar, locomotive, or train brake system;\n**(G)**\ndetermine whether the railroad\u2019s inspection procedures reflect the current operating practices of the railroad carrier; and\n**(H)**\nensure that railroad inspection procedures only provide for the use of persons permitted to perform each relevant inspection under such chapter.\n**(2) Audit scheduling**\nThe Secretary shall\u2014\n**(A)**\nschedule the audits required under paragraph (1) to ensure that\u2014\n**(i)**\nevery Class I railroad is audited not less frequently than once every 5 years; and\n**(ii)**\na limited number, as determined by the Secretary, of Class II and Class III railroads are audited annually, provided that\u2014\n**(I)**\nno audit of a tourist, scenic, historic, or excursion operation may be required under this subsection; and\n**(II)**\nno other Class II or III railroad may be audited more frequently than once every 5 years; and\n**(B)**\nconduct the audits described in subparagraph (A)(ii) in accordance with\u2014\n**(i)**\nthe Small Business Regulatory Enforcement Fairness Act of 1996 ( 5 U.S.C. 601 note); and\n**(ii)**\nappendix C of part 209 of title 49, Code of Federal Regulations.\n**(3) Updates to inspection program and procedures**\nIf, during an audit required under this subsection, the auditor identifies a deficiency in a railroad\u2019s procedures or practices necessary to ensure compliance with chapter II of subtitle B of title 49, Code of Federal Regulations, the railroad shall eliminate such deficiency, after first being provided the opportunity to address whether such a deficiency exists.\n**(4) Consultation and cooperation**\n**(A) Consultation**\nIn conducting any audit required under this subsection, the Secretary shall consult with the railroad being audited and its employees, including any nonprofit employee labor organization representing the employees of the railroad that conduct railcar, locomotive, or train brake system inspections.\n**(B) Cooperation**\nThe railroad being audited and its employees, including any nonprofit employee labor organization representing mechanical employees, shall fully cooperate with any audit conducted pursuant to this subsection\u2014\n**(i)**\nby providing any relevant documents requested; and\n**(ii)**\nby making available any employees for interview without undue delay or obstruction.\n**(C) Failure to cooperate**\nIf the Secretary determines that a railroad or any of its employees, including any nonprofit employee labor organization representing mechanical employees of the railroad is not fully cooperating with an audit conducted pursuant to this subsection, the Secretary shall electronically notify the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives of such noncooperation.\n##### (e) Review of regulations\nNot later than 5 years after the date of the enactment of this Act, and periodically thereafter, the Secretary shall determine whether any update to chapters I and II of subtitle B of title 49, Code of Federal Regulations, is necessary to ensure the adequacy of railcar, locomotive, and train brake system inspections.\n##### (f) Annual report\nThe Secretary shall publish an annual report on the public website of the Federal Railroad Administration that\u2014\n**(1)**\nsummarizes the findings of the audits conducted pursuant to subsection (c) during the most recently concluded fiscal year;\n**(2)**\nsummarizes any updates made to chapter I or II of subtitle B of title 49, Code of Federal Regulations, pursuant to this section; and\n**(3)**\nexcludes any confidential business information or sensitive security information.\n##### (g) Rule of construction\nNothing in this section may be construed\u2014\n**(1)**\nto provide the Secretary with any authority to interpret, revise, alter, or apply a collectively bargained agreement, nor any authority over collective bargaining, collectively bargained agreements, or any aspect of the Railway Labor Act ( 45 U.S.C. 151 et seq. );\n**(2)**\nto alter the terms or interpretations of existing collective bargaining agreements; or\n**(3)**\nto abridge any procedural rights or remedies provided under a collectively bargained agreement.\n#### 5. Defect detectors\n##### (a) Rulemaking\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall issue regulations establishing requirements for the installation, repair, testing, maintenance, and operation of wayside defect detectors for each rail carrier operating a train consist carrying hazardous materials.\n##### (b) Requirements\nThe regulations issued pursuant to subsection (a) shall include requirements regarding\u2014\n**(1)**\nthe frequency of the placement of wayside defect detectors, including a requirement that all Class I railroads install a hotbox detector along every 10-mile segment of rail track over which trains carrying hazardous materials operate;\n**(2)**\nperformance standards for such detectors;\n**(3)**\nthe maintenance and repair requirements for such detectors;\n**(4)**\nreporting data and maintenance records of such detectors;\n**(5)**\nappropriate steps the rail carrier must take when receiving an alert of a defect or failure from or regarding a wayside defect detector; and\n**(6)**\nthe use of hotbox detectors to prevent derailments from wheel bearing failures, including\u2014\n**(A)**\nthe temperatures, to be specified by the Secretary, at which an alert from a hotbox detector is triggered to warn of a potential wheel bearing failure; and\n**(B)**\nany actions that shall be taken by a rail carrier upon receiving an alert from a hotbox detector of a potential wheel bearing failure.\n##### (c) Defect and failure identification\nThe Secretary shall specify the categories of defects and failures that wayside defect detectors covered by regulations issued pursuant to subsection (a) shall address, including\u2014\n**(1)**\naxles;\n**(2)**\nwheel bearings;\n**(3)**\nbrakes;\n**(4)**\nsignals;\n**(5)**\nwheel impacts; and\n**(6)**\nother defects or failures specified by the Secretary.\n##### (d) Safety placards\n**(1) In general**\nIn issuing regulations under subsection (a), the Secretary shall require that placards covered under section 172.519 of title 49, Code of Federal Regulations, be able to withstand heat in excess of 180 degrees.\n**(2) Update based on recommendations**\nThe Secretary may, upon recommendation from the National Transportation Safety Board, issue such regulations as are necessary to increase the heat threshold described in paragraph (1).\n#### 6. Increasing maximum civil penalties for violations of rail safety regulations\n##### (a) Civil penalties related to transporting hazardous materials\nSection 5123(a) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), in the matter preceding subparagraph (A), by striking $75,000 and inserting the greater of 0.5 percent of the person's annual income or annual operating income or $750,000 ; and\n**(2)**\nin paragraph (2), by striking $175,000 and inserting the greater of 1 percent of the person's annual income or annual operating income or $1,750,000 .\n##### (b) General violations of chapter 201\nSection 21301(a)(2) of title 49, United States Code, is amended\u2014\n**(1)**\nby striking $25,000. and inserting the greater of 0.5 percent of the person's annual income or annual operating income or $250,000 ; and\n**(2)**\nby striking $100,000. and inserting the greater of 1 percent of the person's annual income or annual operating income or $1,000,000 .\n##### (c) Accident and incident violations of chapter 201; violations of chapters 203 through 209\nSection 21302(a) is amended\u2014\n**(1)**\nin paragraph (1), by striking 203\u2013209 each place it appears and inserting 203 through 209 ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking $25,000 and inserting the greater of 0.5 percent of the person's annual income or annual operating income or $250,000 ; and\n**(B)**\nby striking $100,000 and inserting the greater of 1 percent of the person's annual income or annual operating income or $1,000,000 .\n##### (d) Violations of chapter 211\nSection 21303(a)(2) is amended\u2014\n**(1)**\nby striking $25,000. and inserting the greater of 0.5 percent of the person's annual income or annual operating income or $250,000 ; and\n**(2)**\nby striking $100,000. and inserting the greater of 1 percent of the person's annual income or annual operating income or $1,000,000 .\n#### 7. Safer tank cars\n##### (a) Phase-Out schedule\nBeginning on May 1, 2030, a rail carrier may not use DOT\u2013111 specification railroad tank cars that do not comply with DOT\u2013117, DOT\u2013117P, or DOT\u2013117R specification requirements, as in effect on the date of enactment of this Act, to transport Class 3 flammable liquids regardless of the composition of the train consist.\n##### (b) Conforming regulatory amendments\n**(1) In general**\nThe Secretary\u2014\n**(A)**\nshall immediately remove or revise the date-specific deadlines in any applicable regulations or orders to the extent necessary to conform with the requirement under subsection (a); and\n**(B)**\nmay not enforce any date-specific deadlines or requirements that are inconsistent with the requirement under subsection (a).\n**(2) Rule of construction**\nExcept as required under paragraph (1), nothing in this section may be construed to require the Secretary to issue regulations to implement this section.\n#### 8. Hazardous materials training for first responders\n##### (a) Annual registration fee\nSection 5108(g) of title 49, United States Code, is amended by adding at the end the following:\n(4) Additional fee for class I rail carriers In addition to the fees collected pursuant to paragraphs (1) and (2), the Secretary shall establish and annually impose and collect from each Class I rail carrier a fee in an amount equal to $1,000,000. .\n##### (b) Assistance for local emergency response training\nSection 5116(j)(1)(A) of title 49, United States Code, is amended\u2014\n**(1)**\nby striking liquids and inserting materials ; and\n**(2)**\nin paragraph (3), by amending subparagraph (A) to read as follows:\n(A) In general To carry out the grant program established pursuant to paragraph (1), the Secretary may expend, during each fiscal year\u2014 (i) the amounts collected pursuant to section 5108(g)(4); and (ii) any amounts recovered during such fiscal year from grants awarded under this section during a prior fiscal year. .\n##### (c) Supplemental training grants\nSection 5128(b)(4) of title 49, United States Code is amended by striking $2,000,000 and inserting $4,000,000 .\n#### 9. Freight train crew size safety standards\n##### (a) Freight train crew size\nSubchapter II of chapter 201 of title 49, United States Code, is amended by inserting after section 20153 the following:\n20154. Freight train crew size safety standards (a) Minimum crew size Except as provided in subsection (b), no Class I railroad carrier may operate a freight train without a 2-person crew consisting of at least 1 appropriately qualified and certified conductor and 1 appropriately qualified and certified locomotive engineer. (b) Exceptions (1) In general Except as provided in paragraph (2), the requirement under subsection (a) shall not apply with respect to\u2014 (A) train operations on track that is not main line track; (B) locomotives performing assistance to a train that has incurred mechanical failure or lacks the power to traverse difficult terrain, including traveling to or from the location where assistance is provided; (C) locomotives that\u2014 (i) are not attached to any equipment or are attached only to a caboose; and (ii) travel not farther than 50 miles from the point of origin of such locomotive; and (D) train operations staffed with fewer than a 2-person crew at least 1 year before the date of the enactment of the Safe Freight Act of 2024, except if the Secretary determines that such operations do not achieve an equivalent level of safety as would result from compliance with the requirement under subsection (a). (2) Trains ineligible for exception The exceptions under paragraph (2) shall not apply with respect to\u2014 (A) a high-hazard train; or (B) a train with a total length of at least 7,500 feet. (c) Waiver A railroad carrier may seek a waiver of the requirements under subsection (a) in accordance with section 20103(d). (d) Definitions In this section: (1) High-hazard train The term high-hazard train means a single train transporting, throughout the train consist\u2014 (A) not fewer than 20 tank cars loaded with a flammable liquid (Class 3) (as such term is defined in section 173.120 of title 49, Code of Federal Regulations, or successor regulations); (B) not fewer than 1 tank car or intermodal portable tank load with a material poisonous by inhalation or a material toxic by inhalation (as such term is defined in section 171.8 of title 49, Code of Federal Regulations, or successor regulations); (C) not fewer than 1 car loaded with a type B package or a fissile material package (as such terms are defined in section 173.403 of title 49, Code of Federal Regulations, or successor regulations); (D) not fewer than 10 cars loaded with Class 1 explosives categorized under section 173.50 of title 49, Code of Federal Regulations (or successor regulations) as being in division 1.1, 1.2, or 1.3; (E) not fewer than 5 tank cars loaded with a flammable gas (as such term is defined in section 173.115(a) of title 49, Code of Federal Regulations, or successor regulations); or (F) not fewer than 20 cars loaded with any combination of flammable liquids, flammable gases, or explosives. (2) Main line track The term main line track means\u2014 (A) a segment or route of railroad tracks\u2014 (i) over which 5,000,000 or more gross tons of railroad traffic is transported annually; and (ii) that has a maximum authorized speed for freight trains in excess of 25 miles per hours; and (B) intercity rail passenger transportation or commuter rail passenger transportation routes or segments over which high-hazard trains operate. .\n##### (b) Clerical amendment\nThe analysis for subchapter II of chapter 201 of title 49, United States Code, is amended by inserting after the item relating to section 20153 the following:\n20154. Freight train crew size safety standards. .\n##### (c) Preservation of authority of secretary\nNothing in section 20154 of title 49, United States Code, as added by this section, shall be construed to limit the authority of the Secretary under any other provision of law.",
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
        "updateDate": "2025-03-07T13:05:56Z"
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
          "measure-id": "id119hr971",
          "measure-number": "971",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr971v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Reducing Accidents In Locomotives Act or the RAIL Act</strong></p><p>This bill addresses safety requirements for rail carriers and trains transporting hazardous materials.</p><p>Specifically, the Department of Transportation (DOT) must issue safety regulations for trains carrying hazardous materials to require that rail carriers (1) provide state emergency response commissioners with advance notice and information about the hazardous materials; (2) reduce blocked rail crossings; and (3) comply with certain requirements regarding train length and weight specifications, track standards, speed restrictions, and response plans.</p><p>DOT must also establish requirements for wayside defect detectors. These are used by railway systems alongside the tracks to detect defects and failures (e.g., wheel bearing failures). Current federal regulations do not require their use, but federal guidance does address their placement and use. Under the bill, DOT must issue regulations establishing requirements for the installation, repair, testing, maintenance, and operation of wayside defect detectors for each rail carrier operating a train carrying hazardous materials.</p><p>Further, DOT must\u00a0update rail car inspection regulations and audit related inspection programs. This includes prohibiting a railroad from limiting the time required for an employee to complete a railcar, locomotive, or brake safety inspection.</p><p>The bill also</p><ul><li>increases the maximum fines DOT may impose on rail carriers for violating safety regulations;</li><li>establishes a statutory requirement\u00a0for freight trains to have at least two crew\u00a0members, with exceptions;</li><li>phases out certain railroad tank cars by May 1,\u00a02030;</li><li>expands training for local first responders; and</li><li>imposes a new fee on certain rail carriers.</li></ul>"
        },
        "title": "RAIL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr971.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reducing Accidents In Locomotives Act or the RAIL Act</strong></p><p>This bill addresses safety requirements for rail carriers and trains transporting hazardous materials.</p><p>Specifically, the Department of Transportation (DOT) must issue safety regulations for trains carrying hazardous materials to require that rail carriers (1) provide state emergency response commissioners with advance notice and information about the hazardous materials; (2) reduce blocked rail crossings; and (3) comply with certain requirements regarding train length and weight specifications, track standards, speed restrictions, and response plans.</p><p>DOT must also establish requirements for wayside defect detectors. These are used by railway systems alongside the tracks to detect defects and failures (e.g., wheel bearing failures). Current federal regulations do not require their use, but federal guidance does address their placement and use. Under the bill, DOT must issue regulations establishing requirements for the installation, repair, testing, maintenance, and operation of wayside defect detectors for each rail carrier operating a train carrying hazardous materials.</p><p>Further, DOT must\u00a0update rail car inspection regulations and audit related inspection programs. This includes prohibiting a railroad from limiting the time required for an employee to complete a railcar, locomotive, or brake safety inspection.</p><p>The bill also</p><ul><li>increases the maximum fines DOT may impose on rail carriers for violating safety regulations;</li><li>establishes a statutory requirement\u00a0for freight trains to have at least two crew\u00a0members, with exceptions;</li><li>phases out certain railroad tank cars by May 1,\u00a02030;</li><li>expands training for local first responders; and</li><li>imposes a new fee on certain rail carriers.</li></ul>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr971"
    },
    "title": "RAIL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reducing Accidents In Locomotives Act or the RAIL Act</strong></p><p>This bill addresses safety requirements for rail carriers and trains transporting hazardous materials.</p><p>Specifically, the Department of Transportation (DOT) must issue safety regulations for trains carrying hazardous materials to require that rail carriers (1) provide state emergency response commissioners with advance notice and information about the hazardous materials; (2) reduce blocked rail crossings; and (3) comply with certain requirements regarding train length and weight specifications, track standards, speed restrictions, and response plans.</p><p>DOT must also establish requirements for wayside defect detectors. These are used by railway systems alongside the tracks to detect defects and failures (e.g., wheel bearing failures). Current federal regulations do not require their use, but federal guidance does address their placement and use. Under the bill, DOT must issue regulations establishing requirements for the installation, repair, testing, maintenance, and operation of wayside defect detectors for each rail carrier operating a train carrying hazardous materials.</p><p>Further, DOT must\u00a0update rail car inspection regulations and audit related inspection programs. This includes prohibiting a railroad from limiting the time required for an employee to complete a railcar, locomotive, or brake safety inspection.</p><p>The bill also</p><ul><li>increases the maximum fines DOT may impose on rail carriers for violating safety regulations;</li><li>establishes a statutory requirement\u00a0for freight trains to have at least two crew\u00a0members, with exceptions;</li><li>phases out certain railroad tank cars by May 1,\u00a02030;</li><li>expands training for local first responders; and</li><li>imposes a new fee on certain rail carriers.</li></ul>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr971"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr971ih.xml"
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
      "title": "RAIL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RAIL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reducing Accidents In Locomotives Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance safety requirements for trains transporting hazardous materials, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:20Z"
    }
  ]
}
```
