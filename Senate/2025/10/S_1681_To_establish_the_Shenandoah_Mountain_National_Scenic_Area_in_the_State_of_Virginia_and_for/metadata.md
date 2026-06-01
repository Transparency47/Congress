# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1681?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1681
- Title: Shenandoah Mountain Act
- Congress: 119
- Bill type: S
- Bill number: 1681
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-12-11T16:53:22Z
- Update date including text: 2025-12-11T16:53:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 214.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 214.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1681",
    "number": "1681",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Shenandoah Mountain Act",
    "type": "S",
    "updateDate": "2025-12-11T16:53:22Z",
    "updateDateIncludingText": "2025-12-11T16:53:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-27",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 214.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
            "date": "2025-10-27T22:49:31Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-21T20:01:15Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-08T17:02:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1681is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1681\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Kaine (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo establish the Shenandoah Mountain National Scenic Area in the State of Virginia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shenandoah Mountain Act .\n#### 2. Definitions\nIn this Act:\n**(1) National Scenic Area**\n**(A) In general**\nThe term National Scenic Area means the Shenandoah Mountain National Scenic Area established by section 3(a).\n**(B) Inclusions**\nThe term National Scenic Area includes\u2014\n**(i)**\nany National Forest System land within the boundary of the National Scenic Area that is administered as part of the National Scenic Area; and\n**(ii)**\nany National Forest System land within the boundary of the National Scenic Area that is administered as a component of the National Wilderness Preservation System under the amendments made by section 4.\n**(2) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n**(3) State**\nThe term State means the State of Virginia.\n**(4) Wilderness Area**\nThe term Wilderness Area means a wilderness area designated by paragraphs (21) through (25) of section 1 of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584; 114 Stat. 2057; 123 Stat. 1002) (as added by section 4).\n#### 3. Establishment of the Shenandoah Mountain National Scenic Area\n##### (a) Establishment\nSubject to valid existing rights, there is established the Shenandoah Mountain National Scenic Area, consisting of approximately 92,562 acres of National Forest System land in the George Washington and Jefferson National Forests, as generally depicted on the map filed under section 5(a)(1).\n##### (b) Purposes\nThe purposes of the National Scenic Area are\u2014\n**(1)**\nto ensure the protection and preservation of the scenic quality, water quality, natural characteristics, and water resources of the National Scenic Area;\n**(2)**\nto protect wildlife, fish, and plant habitat in the National Scenic Area;\n**(3)**\nto protect outstanding natural biological values and habitat for plant and animal species along the Shenandoah Mountain crest above 3,000 feet above sea level elevation, including the Cow Knob salamander;\n**(4)**\nto protect forests in the National Scenic Area that may develop characteristics of old-growth forests;\n**(5)**\nto protect the Wilderness Areas; and\n**(6)**\nto provide for a variety of, and improve existing, recreation settings and opportunities in the National Scenic Area in a manner consistent with the purposes of the National Scenic Area described in paragraphs (1) through (5).\n##### (c) Administration\n**(1) In general**\nExcept as provided in paragraph (2), the Secretary shall administer the National Scenic Area in accordance with\u2014\n**(A)**\nthis section; and\n**(B)**\nthe laws (including regulations) generally applicable to the National Forest System.\n**(2) Exception**\nSubject to valid existing rights, the Secretary shall administer the Wilderness Areas in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ) and any other laws applicable to the Wilderness Areas, except that any reference in that Act to the effective date of that Act shall be considered to be a reference to the date of enactment of this Act for purposes of administering the Wilderness Areas.\n**(3) Effect; conflicts**\n**(A) Effect**\nThe establishment of the National Scenic Area shall not affect the administration of the Wilderness Areas.\n**(B) Conflicts**\nIn the case of any conflict between the laws applicable to the Wilderness Areas, the Wilderness Act ( 16 U.S.C. 1131 et seq. ) shall control.\n**(4) No buffer zones**\n**(A) In general**\nNothing in this section creates a protective perimeter or buffer zone around the National Scenic Area or a Wilderness Area.\n**(B) Activities outside National Scenic Area or Wilderness Areas**\nThe fact that an activity or use on land outside the National Scenic Area or a Wilderness Area can be seen or heard by humans within the National Scenic Area or Wilderness Area shall not preclude the activity or use outside the boundaries of the National Scenic Area or Wilderness Area.\n##### (d) Recreational uses\n**(1) In general**\nExcept as otherwise provided in this section or under applicable law, the Secretary shall authorize the continuation of, or seek to improve, authorized recreational uses of the National Scenic Area in existence on the date of enactment of this Act.\n**(2) Effect**\nNothing in this section interferes with the authority of the Secretary\u2014\n**(A)**\nto maintain or improve nonmotorized trails and recreation sites within the National Scenic Area;\n**(B)**\nto construct new nonmotorized trails and recreation sites within the National Scenic Area;\n**(C)**\nto adjust recreational uses within the National Scenic Area for reasons of sound resource management or public safety; and\n**(D)**\nto evaluate applications for, and issue or deny, special use authorizations in connection with recreation within the National Scenic Area.\n**(3) Requirement**\nRecreation within the National Scenic Area shall be conducted in a manner consistent with the purposes of the National Scenic Area described in subsection (b).\n##### (e) National Forest System trail plan\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall develop a National Forest System trail plan for National Forest System land in the National Scenic Area that is not located in a Wilderness Area in order to construct, maintain, and improve nonmotorized recreation National Forest System trails in a manner consistent with the purposes of the National Scenic Area described in subsection (b).\n**(2) Potential inclusion**\nThe Secretary may address in the National Forest System trail plan developed under paragraph (1) National Forest System land that is near, but not within the boundary of, the National Scenic Area.\n**(3) Public input**\nIn developing the National Forest System trail plan under paragraph (1), the Secretary shall seek input from interested parties, including members of the public.\n**(4) Requirements**\nThe National Forest System trail plan developed under paragraph (1) shall\u2014\n**(A)**\npromote sustainable trail management that protects natural resources and provides diverse, high-quality recreation opportunities, which may include loop trails for nonmotorized uses;\n**(B)**\nconsider natural resource protection, trail sustainability, and trail maintenance needs as primary factors in determining the location or relocation of National Forest System trails; and\n**(C)**\ndevelop a National Forest System trail outside the Little River Wilderness Area in the area of the Tillman Road corridor (along National Forest System road 101) to connect the Wolf Ridge Trail parking area to the Wild Oak National Recreation Trail, as generally depicted on the applicable map filed under section 5(a)(2), pending completion of the required environmental analysis.\n**(5) Implementation report**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall submit to Congress a report that describes the implementation of the National Forest System trail plan developed under paragraph (1), including the identification of the National Forest System trail described in paragraph (4)(C) and any other priority National Forest System trails identified for development.\n##### (f) Roads\n**(1) In general**\nThe establishment of the National Scenic Area shall not\u2014\n**(A)**\nresult in the closure of any National Forest System roads, as generally depicted on the map filed under section 5(a)(1); or\n**(B)**\nmodify public access within the National Scenic Area.\n**(2) No new roads**\nNo new roads shall be constructed in the National Scenic Area after the date of enactment of this Act.\n**(3) Effect**\nNothing in this section\u2014\n**(A)**\ndenies any owner of private land or an interest in private land that is located within the National Scenic Area the right to access the private land;\n**(B)**\nalters the authority of the Secretary to open or close roads in the National Scenic Area in existence on the date of enactment of this Act in furtherance of the purposes of this Act; or\n**(C)**\nalters the authority of the State\u2014\n**(i)**\nto maintain the access road to the crest of Shenandoah Mountain (Route 924); or\n**(ii)**\nto realign the access road described in clause (i) if necessary for reasons of sound resource management or public safety.\n**(4) Parking areas**\n**(A) In general**\nSubject to subparagraph (B), the reconstruction, minor relocation, and construction of parking areas and related facilities within the National Scenic Area are authorized in a manner consistent with the purposes of the National Scenic Area described in subsection (b).\n**(B) Limitation**\nAdditional trailhead parking areas authorized in the National Scenic Area under subparagraph (A) may be constructed only along National Forest System roads.\n##### (g) Motorized travel\nMotorized travel shall be allowed only on roads within the portions of the National Scenic Area that are not Wilderness Areas, in a manner consistent with subsection (f).\n##### (h) Water\nThe Secretary shall administer the National Scenic Area in a manner that maintains and enhances water quality.\n##### (i) Water impoundments\nThe establishment of the National Scenic Area shall not prohibit\u2014\n**(1)**\nthe operation, maintenance, or improvement of, or access to, dams, reservoirs, or related infrastructure in existence on the date of enactment of this Act, as generally depicted on the map filed under section 5(a)(1); or\n**(2)**\nthe establishment of new dams, reservoirs, or related infrastructure if necessary for municipal use.\n##### (j) Timber harvest\n**(1) In general**\nExcept as provided in paragraph (2), no harvesting of timber shall be allowed within the National Scenic Area.\n**(2) Exceptions**\n**(A) Necessary harvesting**\nThe Secretary may authorize harvesting of timber in the National Scenic Area if the Secretary determines that the harvesting is necessary\u2014\n**(i)**\nto control fire;\n**(ii)**\nto provide for public safety or trail access;\n**(iii)**\nto construct or maintain overlooks and vistas; or\n**(iv)**\nto control insect or disease outbreaks.\n**(B) Firewood for personal use**\nFirewood may be harvested for personal use along roads within the National Scenic Area, subject to any conditions that the Secretary may require.\n##### (k) Insect and disease outbreaks\n**(1) In general**\nSubject to paragraph (2), the Secretary may carry out activities necessary to control insect and disease outbreaks in a manner consistent with the purposes of the National Scenic Area described in subsection (b)\u2014\n**(A)**\nto maintain scenic quality;\n**(B)**\nto reduce hazards to visitors; or\n**(C)**\nto protect National Forest System land or private land.\n**(2) Limitations**\nFor purposes of activities carried out under paragraph (1)\u2014\n**(A)**\nnative forest insect and disease outbreaks shall be controlled only\u2014\n**(i)**\nto prevent unacceptable damage to resources on adjacent land; or\n**(ii)**\nto protect threatened, endangered, sensitive, or locally rare species, with biological control methods being favored; and\n**(B)**\nnonnative insects and diseases may be eradicated or suppressed only in order to prevent a loss of a special biological community.\n##### (l) Vegetation management\nThe Secretary may engage in vegetation management practices within the National Scenic Area in a manner consistent with the purposes of the National Scenic Area described in subsection (b)\u2014\n**(1)**\nto maintain wildlife clearings and scenic enhancements in existence on the date of enactment of this Act; or\n**(2)**\nto construct not more than 100 acres of additional wildlife clearings by\u2014\n**(A)**\nexpanding wildlife clearings in existence on the date of enactment of this Act; or\n**(B)**\nconstructing new wildlife clearings of approximately 2 to 5 acres.\n##### (m) Wildfire suppression\n**(1) In general**\nNothing in this section prohibits the Secretary, in cooperation with other Federal, State, and local agencies, as appropriate, from carrying out wildfire suppression activities within the National Scenic Area.\n**(2) Requirements**\nWildfire suppression activities within the National Scenic Area shall be carried out\u2014\n**(A)**\nin a manner consistent with the purposes of the National Scenic Area described in subsection (b); and\n**(B)**\nusing such means as the Secretary determines to be appropriate.\n##### (n) Prescribed fire\nNothing in this section prohibits the Secretary from conducting prescribed burns and necessary burn unit preparation within the National Scenic Area in a manner consistent with the purposes of the National Scenic Area described in subsection (b).\n##### (o) Withdrawal\n**(1) In general**\nSubject to valid existing rights, all Federal land within the National Scenic Area is withdrawn from\u2014\n**(A)**\nentry, appropriation, or disposal under the public land laws;\n**(B)**\nlocation, entry, and patent under the mining laws;\n**(C)**\noperation of the mineral leasing and geothermal leasing laws;\n**(D)**\nwind, solar, or other renewable energy development; and\n**(E)**\ndesignation of new utility corridors, utility rights-of-way, or communications sites.\n**(2) Effect**\nConsistent with subsection (f)(3)(A), the withdrawal under paragraph (1) shall not deny access to private land or an interest in private land within the National Scenic Area.\n##### (p) Management plan\n**(1) In general**\nAs soon as practicable after the date of the completion of the National Forest System trail plan under subsection (e), but not later than 2 years after the date of enactment of this Act, the Secretary shall develop as an amendment to the land management plan for the George Washington and Jefferson National Forests a management plan for the National Scenic Area that is consistent with this section.\n**(2) Effect**\nNothing in this subsection requires the Secretary to revise the land management plan for the George Washington and Jefferson National Forests under section 6 of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1604 ).\n#### 4. Designation of wilderness areas\nSection 1 of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584; 114 Stat. 2057; 123 Stat. 1002) is amended by adding at the end the following:\n(21) Skidmore fork wilderness Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 5,088 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be known as the Skidmore Fork Wilderness . (22) Ramseys draft wilderness addition Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 6,961 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be incorporated into the Ramseys Draft Wilderness designated by Public Law 98\u2013586 ( 16 U.S.C. 1132 note; 98 Stat. 3106). (23) Lynn hollow wilderness Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 3,568 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be known as the Lynn Hollow Wilderness . (24) Little river wilderness Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 12,461 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be known as the Little River Wilderness . (25) Beech lick knob wilderness Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 5,779 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be known as the Beech Lick Knob Wilderness . .\n#### 5. Maps and boundary descriptions\n##### (a) Filing\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file with the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Natural Resources and the Committee on Agriculture of the House of Representatives maps and boundary descriptions of\u2014\n**(1)**\nthe National Scenic Area; and\n**(2)**\neach of the Wilderness Areas.\n##### (b) Force and effect\nThe maps and boundary descriptions filed under subsection (a) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the maps and boundary descriptions.\n##### (c) Maps control\nIn the case of any discrepancy between the acreage of the National Scenic Area or a Wilderness Area and the applicable map filed under subsection (a), the applicable map filed under that subsection shall control.\n##### (d) Availability\nThe maps and boundary descriptions filed under subsection (a) shall be on file and available for public inspection in the office of the Chief of the Forest Service.",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1681rs.xml",
      "text": "II\nCalendar No. 214\n119th CONGRESS\n1st Session\nS. 1681\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Kaine (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nOctober 27, 2025 Reported by Mr. Boozman , without amendment\nA BILL\nTo establish the Shenandoah Mountain National Scenic Area in the State of Virginia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shenandoah Mountain Act .\n#### 2. Definitions\nIn this Act:\n**(1) National Scenic Area**\n**(A) In general**\nThe term National Scenic Area means the Shenandoah Mountain National Scenic Area established by section 3(a).\n**(B) Inclusions**\nThe term National Scenic Area includes\u2014\n**(i)**\nany National Forest System land within the boundary of the National Scenic Area that is administered as part of the National Scenic Area; and\n**(ii)**\nany National Forest System land within the boundary of the National Scenic Area that is administered as a component of the National Wilderness Preservation System under the amendments made by section 4.\n**(2) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n**(3) State**\nThe term State means the State of Virginia.\n**(4) Wilderness Area**\nThe term Wilderness Area means a wilderness area designated by paragraphs (21) through (25) of section 1 of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584; 114 Stat. 2057; 123 Stat. 1002) (as added by section 4).\n#### 3. Establishment of the Shenandoah Mountain National Scenic Area\n##### (a) Establishment\nSubject to valid existing rights, there is established the Shenandoah Mountain National Scenic Area, consisting of approximately 92,562 acres of National Forest System land in the George Washington and Jefferson National Forests, as generally depicted on the map filed under section 5(a)(1).\n##### (b) Purposes\nThe purposes of the National Scenic Area are\u2014\n**(1)**\nto ensure the protection and preservation of the scenic quality, water quality, natural characteristics, and water resources of the National Scenic Area;\n**(2)**\nto protect wildlife, fish, and plant habitat in the National Scenic Area;\n**(3)**\nto protect outstanding natural biological values and habitat for plant and animal species along the Shenandoah Mountain crest above 3,000 feet above sea level elevation, including the Cow Knob salamander;\n**(4)**\nto protect forests in the National Scenic Area that may develop characteristics of old-growth forests;\n**(5)**\nto protect the Wilderness Areas; and\n**(6)**\nto provide for a variety of, and improve existing, recreation settings and opportunities in the National Scenic Area in a manner consistent with the purposes of the National Scenic Area described in paragraphs (1) through (5).\n##### (c) Administration\n**(1) In general**\nExcept as provided in paragraph (2), the Secretary shall administer the National Scenic Area in accordance with\u2014\n**(A)**\nthis section; and\n**(B)**\nthe laws (including regulations) generally applicable to the National Forest System.\n**(2) Exception**\nSubject to valid existing rights, the Secretary shall administer the Wilderness Areas in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ) and any other laws applicable to the Wilderness Areas, except that any reference in that Act to the effective date of that Act shall be considered to be a reference to the date of enactment of this Act for purposes of administering the Wilderness Areas.\n**(3) Effect; conflicts**\n**(A) Effect**\nThe establishment of the National Scenic Area shall not affect the administration of the Wilderness Areas.\n**(B) Conflicts**\nIn the case of any conflict between the laws applicable to the Wilderness Areas, the Wilderness Act ( 16 U.S.C. 1131 et seq. ) shall control.\n**(4) No buffer zones**\n**(A) In general**\nNothing in this section creates a protective perimeter or buffer zone around the National Scenic Area or a Wilderness Area.\n**(B) Activities outside National Scenic Area or Wilderness Areas**\nThe fact that an activity or use on land outside the National Scenic Area or a Wilderness Area can be seen or heard by humans within the National Scenic Area or Wilderness Area shall not preclude the activity or use outside the boundaries of the National Scenic Area or Wilderness Area.\n##### (d) Recreational uses\n**(1) In general**\nExcept as otherwise provided in this section or under applicable law, the Secretary shall authorize the continuation of, or seek to improve, authorized recreational uses of the National Scenic Area in existence on the date of enactment of this Act.\n**(2) Effect**\nNothing in this section interferes with the authority of the Secretary\u2014\n**(A)**\nto maintain or improve nonmotorized trails and recreation sites within the National Scenic Area;\n**(B)**\nto construct new nonmotorized trails and recreation sites within the National Scenic Area;\n**(C)**\nto adjust recreational uses within the National Scenic Area for reasons of sound resource management or public safety; and\n**(D)**\nto evaluate applications for, and issue or deny, special use authorizations in connection with recreation within the National Scenic Area.\n**(3) Requirement**\nRecreation within the National Scenic Area shall be conducted in a manner consistent with the purposes of the National Scenic Area described in subsection (b).\n##### (e) National Forest System trail plan\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall develop a National Forest System trail plan for National Forest System land in the National Scenic Area that is not located in a Wilderness Area in order to construct, maintain, and improve nonmotorized recreation National Forest System trails in a manner consistent with the purposes of the National Scenic Area described in subsection (b).\n**(2) Potential inclusion**\nThe Secretary may address in the National Forest System trail plan developed under paragraph (1) National Forest System land that is near, but not within the boundary of, the National Scenic Area.\n**(3) Public input**\nIn developing the National Forest System trail plan under paragraph (1), the Secretary shall seek input from interested parties, including members of the public.\n**(4) Requirements**\nThe National Forest System trail plan developed under paragraph (1) shall\u2014\n**(A)**\npromote sustainable trail management that protects natural resources and provides diverse, high-quality recreation opportunities, which may include loop trails for nonmotorized uses;\n**(B)**\nconsider natural resource protection, trail sustainability, and trail maintenance needs as primary factors in determining the location or relocation of National Forest System trails; and\n**(C)**\ndevelop a National Forest System trail outside the Little River Wilderness Area in the area of the Tillman Road corridor (along National Forest System road 101) to connect the Wolf Ridge Trail parking area to the Wild Oak National Recreation Trail, as generally depicted on the applicable map filed under section 5(a)(2), pending completion of the required environmental analysis.\n**(5) Implementation report**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall submit to Congress a report that describes the implementation of the National Forest System trail plan developed under paragraph (1), including the identification of the National Forest System trail described in paragraph (4)(C) and any other priority National Forest System trails identified for development.\n##### (f) Roads\n**(1) In general**\nThe establishment of the National Scenic Area shall not\u2014\n**(A)**\nresult in the closure of any National Forest System roads, as generally depicted on the map filed under section 5(a)(1); or\n**(B)**\nmodify public access within the National Scenic Area.\n**(2) No new roads**\nNo new roads shall be constructed in the National Scenic Area after the date of enactment of this Act.\n**(3) Effect**\nNothing in this section\u2014\n**(A)**\ndenies any owner of private land or an interest in private land that is located within the National Scenic Area the right to access the private land;\n**(B)**\nalters the authority of the Secretary to open or close roads in the National Scenic Area in existence on the date of enactment of this Act in furtherance of the purposes of this Act; or\n**(C)**\nalters the authority of the State\u2014\n**(i)**\nto maintain the access road to the crest of Shenandoah Mountain (Route 924); or\n**(ii)**\nto realign the access road described in clause (i) if necessary for reasons of sound resource management or public safety.\n**(4) Parking areas**\n**(A) In general**\nSubject to subparagraph (B), the reconstruction, minor relocation, and construction of parking areas and related facilities within the National Scenic Area are authorized in a manner consistent with the purposes of the National Scenic Area described in subsection (b).\n**(B) Limitation**\nAdditional trailhead parking areas authorized in the National Scenic Area under subparagraph (A) may be constructed only along National Forest System roads.\n##### (g) Motorized travel\nMotorized travel shall be allowed only on roads within the portions of the National Scenic Area that are not Wilderness Areas, in a manner consistent with subsection (f).\n##### (h) Water\nThe Secretary shall administer the National Scenic Area in a manner that maintains and enhances water quality.\n##### (i) Water impoundments\nThe establishment of the National Scenic Area shall not prohibit\u2014\n**(1)**\nthe operation, maintenance, or improvement of, or access to, dams, reservoirs, or related infrastructure in existence on the date of enactment of this Act, as generally depicted on the map filed under section 5(a)(1); or\n**(2)**\nthe establishment of new dams, reservoirs, or related infrastructure if necessary for municipal use.\n##### (j) Timber harvest\n**(1) In general**\nExcept as provided in paragraph (2), no harvesting of timber shall be allowed within the National Scenic Area.\n**(2) Exceptions**\n**(A) Necessary harvesting**\nThe Secretary may authorize harvesting of timber in the National Scenic Area if the Secretary determines that the harvesting is necessary\u2014\n**(i)**\nto control fire;\n**(ii)**\nto provide for public safety or trail access;\n**(iii)**\nto construct or maintain overlooks and vistas; or\n**(iv)**\nto control insect or disease outbreaks.\n**(B) Firewood for personal use**\nFirewood may be harvested for personal use along roads within the National Scenic Area, subject to any conditions that the Secretary may require.\n##### (k) Insect and disease outbreaks\n**(1) In general**\nSubject to paragraph (2), the Secretary may carry out activities necessary to control insect and disease outbreaks in a manner consistent with the purposes of the National Scenic Area described in subsection (b)\u2014\n**(A)**\nto maintain scenic quality;\n**(B)**\nto reduce hazards to visitors; or\n**(C)**\nto protect National Forest System land or private land.\n**(2) Limitations**\nFor purposes of activities carried out under paragraph (1)\u2014\n**(A)**\nnative forest insect and disease outbreaks shall be controlled only\u2014\n**(i)**\nto prevent unacceptable damage to resources on adjacent land; or\n**(ii)**\nto protect threatened, endangered, sensitive, or locally rare species, with biological control methods being favored; and\n**(B)**\nnonnative insects and diseases may be eradicated or suppressed only in order to prevent a loss of a special biological community.\n##### (l) Vegetation management\nThe Secretary may engage in vegetation management practices within the National Scenic Area in a manner consistent with the purposes of the National Scenic Area described in subsection (b)\u2014\n**(1)**\nto maintain wildlife clearings and scenic enhancements in existence on the date of enactment of this Act; or\n**(2)**\nto construct not more than 100 acres of additional wildlife clearings by\u2014\n**(A)**\nexpanding wildlife clearings in existence on the date of enactment of this Act; or\n**(B)**\nconstructing new wildlife clearings of approximately 2 to 5 acres.\n##### (m) Wildfire suppression\n**(1) In general**\nNothing in this section prohibits the Secretary, in cooperation with other Federal, State, and local agencies, as appropriate, from carrying out wildfire suppression activities within the National Scenic Area.\n**(2) Requirements**\nWildfire suppression activities within the National Scenic Area shall be carried out\u2014\n**(A)**\nin a manner consistent with the purposes of the National Scenic Area described in subsection (b); and\n**(B)**\nusing such means as the Secretary determines to be appropriate.\n##### (n) Prescribed fire\nNothing in this section prohibits the Secretary from conducting prescribed burns and necessary burn unit preparation within the National Scenic Area in a manner consistent with the purposes of the National Scenic Area described in subsection (b).\n##### (o) Withdrawal\n**(1) In general**\nSubject to valid existing rights, all Federal land within the National Scenic Area is withdrawn from\u2014\n**(A)**\nentry, appropriation, or disposal under the public land laws;\n**(B)**\nlocation, entry, and patent under the mining laws;\n**(C)**\noperation of the mineral leasing and geothermal leasing laws;\n**(D)**\nwind, solar, or other renewable energy development; and\n**(E)**\ndesignation of new utility corridors, utility rights-of-way, or communications sites.\n**(2) Effect**\nConsistent with subsection (f)(3)(A), the withdrawal under paragraph (1) shall not deny access to private land or an interest in private land within the National Scenic Area.\n##### (p) Management plan\n**(1) In general**\nAs soon as practicable after the date of the completion of the National Forest System trail plan under subsection (e), but not later than 2 years after the date of enactment of this Act, the Secretary shall develop as an amendment to the land management plan for the George Washington and Jefferson National Forests a management plan for the National Scenic Area that is consistent with this section.\n**(2) Effect**\nNothing in this subsection requires the Secretary to revise the land management plan for the George Washington and Jefferson National Forests under section 6 of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1604 ).\n#### 4. Designation of wilderness areas\nSection 1 of Public Law 100\u2013326 ( 16 U.S.C. 1132 note; 102 Stat. 584; 114 Stat. 2057; 123 Stat. 1002) is amended by adding at the end the following:\n(21) Skidmore fork wilderness Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 5,088 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be known as the Skidmore Fork Wilderness . (22) Ramseys draft wilderness addition Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 6,961 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be incorporated into the Ramseys Draft Wilderness designated by Public Law 98\u2013586 ( 16 U.S.C. 1132 note; 98 Stat. 3106). (23) Lynn hollow wilderness Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 3,568 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be known as the Lynn Hollow Wilderness . (24) Little river wilderness Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 12,461 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be known as the Little River Wilderness . (25) Beech lick knob wilderness Certain National Forest System land in the George Washington and Jefferson National Forests comprising approximately 5,779 acres, as generally depicted on the applicable map filed under section 5(a)(2) of the Shenandoah Mountain Act , which shall be known as the Beech Lick Knob Wilderness . .\n#### 5. Maps and boundary descriptions\n##### (a) Filing\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file with the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Natural Resources and the Committee on Agriculture of the House of Representatives maps and boundary descriptions of\u2014\n**(1)**\nthe National Scenic Area; and\n**(2)**\neach of the Wilderness Areas.\n##### (b) Force and effect\nThe maps and boundary descriptions filed under subsection (a) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the maps and boundary descriptions.\n##### (c) Maps control\nIn the case of any discrepancy between the acreage of the National Scenic Area or a Wilderness Area and the applicable map filed under subsection (a), the applicable map filed under that subsection shall control.\n##### (d) Availability\nThe maps and boundary descriptions filed under subsection (a) shall be on file and available for public inspection in the office of the Chief of the Forest Service.",
      "versionDate": "2025-10-27",
      "versionType": "Reported in Senate"
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
            "name": "Congressional oversight",
            "updateDate": "2025-12-11T16:53:03Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-12-11T16:53:12Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-11T16:52:45Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-12-11T16:53:22Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-12-11T16:53:17Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-11T16:52:57Z"
          },
          {
            "name": "Pest management",
            "updateDate": "2025-12-11T16:53:08Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2025-12-11T16:52:38Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-11T16:52:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-11T13:57:25Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1681is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1681rs.xml"
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
      "title": "Shenandoah Mountain Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-29T06:08:15Z"
    },
    {
      "title": "Shenandoah Mountain Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Shenandoah Mountain Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Shenandoah Mountain National Scenic Area in the State of Virginia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:35Z"
    }
  ]
}
```
