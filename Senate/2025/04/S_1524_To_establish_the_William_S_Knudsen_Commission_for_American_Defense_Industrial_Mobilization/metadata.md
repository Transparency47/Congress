# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1524?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1524
- Title: William S. Knudsen Defense Remobilization Act
- Congress: 119
- Bill type: S
- Bill number: 1524
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2025-05-29T17:57:29Z
- Update date including text: 2025-05-29T17:57:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1524",
    "number": "1524",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "William S. Knudsen Defense Remobilization Act",
    "type": "S",
    "updateDate": "2025-05-29T17:57:29Z",
    "updateDateIncludingText": "2025-05-29T17:57:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T15:33:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "AR"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1524is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1524\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Banks (for himself, Mr. Cotton , and Mr. Schmitt ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo establish the William S. Knudsen Commission for American Defense-Industrial Mobilization, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the William S. Knudsen Defense Remobilization Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe United States faces a critical lack of domestic industrial capacity necessary to support and maintain its defense, particularly in the event of a major conflict.\n**(2)**\nCurrent and building shortages of munitions and materiel are estimated to require years to replenish sufficiently.\n**(3)**\nThe domestic industrial base is shaped by Federal Government policies, including by a raft of regulations that often inhibit production and expansion.\n**(4)**\nThe lack of industrial capacity now constituted a major threat to the national security as conflicts supplied with United States arms escalate around the globe and imminent threats to United States interests have emerged.\n**(5)**\nBefore entering World War II, the United States faced a similar crisis of adequate defense production as it supplied its allies in Europe and prepared for the event of war.\n**(6)**\nIn 1940, William S. Knudsen, an American automotive executive, was tasked with coordinating and spearheading the nation\u2019s war production by serving as the chairman of the Office of Production Management and as a member of the National Defense Advisory Commission.\n**(7)**\nAs a result of Mr. Knudsen\u2019s efforts, the United States mobilized an unprecedented industrial war production network, renowned as the Arsenal of Democracy, that enabled Allied victory.\n#### 3. Establishment of the William S. Knudsen Commission for American Defense-Industrial Mobilization\n##### (a) Establishment\nThere is established in the legislative branch the William S. Knudsen Commission for American Defense-Industrial Mobilization (referred to in this Act as the Commission ).\n##### (b) Purpose\nThe purpose of the Commission is to examine and make recommendations to the President and Congress with respect to the defense-industrial base of the United States.\n##### (c) Membership\n**(1) Composition**\nThe Commission shall be composed of 12 members of whom\u2014\n**(A)**\n1 member shall be appointed by the majority leader of the Senate;\n**(B)**\n1 member shall be appointed by the minority leader of the Senate;\n**(C)**\n1 member shall be appointed by the Speaker of the House of Representatives;\n**(D)**\n1 member shall be appointed by the minority leader of the House of Representatives;\n**(E)**\n2 members shall be appointed by the chair of the Committee on Armed Services of the Senate;\n**(F)**\n2 members shall be appointed by the ranking minority member of the Committee on Armed Services of the Senate;\n**(G)**\n2 members shall be appointed by the chair of the Committee on Armed Services of the House of Representatives; and\n**(H)**\n2 members shall be appointed by the ranking minority member of the Committee on Armed Services of the House of Representatives.\n**(2) Qualifications**\nthe members appointed under paragraph (1) shall be from among individuals who\u2014\n**(A)**\nare United States citizens; and\n**(B)**\nhave significant professional experience or expertise in\u2014\n**(i)**\nthe manufacturing sector;\n**(ii)**\ndefense procurement;\n**(iii)**\ndefense technology and innovation; and\n**(iv)**\nindustrial policy.\n**(3) Deadline for appointment**\n**(A) In general**\nAll members of the Commission shall be appointed under paragraph (1) not later than 45 days after the date of the enactment of this Act.\n**(B) Effect of lack of appointments by appointment date**\nIf one or more appointments under paragraph (1) is not made by the date specified in subparagraph (A)\u2014\n**(i)**\nthe authority to make such appointment or appointments shall expire; and\n**(ii)**\nthe number of members of the Commission shall be reduced by the number of appointments not made by that date.\n**(4) Chair; vice chair**\n**(A) Chair**\nThe chairs of the appropriate congressional committees shall jointly designate one member of the Commission to serve as chair of the Commission.\n**(B) Vice chair**\nThe ranking minority members of the appropriate congressional committees shall jointly designate one member of the Commission to serve as vice chair of the Commission.\n**(5) Meetings**\n**(A) Initial meeting**\nThe Commission shall hold the first meeting as soon as practicable after 2/3 of the members of the Commission have been appointed under paragraph (1).\n**(B) Subsequent meetings**\nAfter its initial meeting, the Commission shall meet upon the call of the chair or a majority of its members.\n**(6) Quorum**\nEight members of the Commission shall constitute a quorum for purposes of conducting business.\n**(7) Period of appointment; vacancies**\nMembers of the Commission shall be appointed for the life of the Commission. A vacancy in the Commission does not affect the powers of the Commission and shall (except as provided by paragraph (3)(B)) be filled in the same manner in which the original appointment was made.\n**(8) Removal of members**\n**(A) In general**\nA member of the Commission may be removed from the Commission for cause by the individual serving in the position responsible for the original appointment of the member under paragraph (1), provided that notice is first provided to that official of the cause for removal, and removal is voted and agreed upon by 3/4 of the members of the Commission.\n**(B) Vacancies**\nA vacancy created by the removal of a member of the Commission under subparagraph (A) does not affect the powers of the Commission and shall be filled in the same manner in which the original appointment was made.\n##### (d) Duties\n**(1) Review**\nThe Commission shall conduct a review of the defense industrial base of the United States, including an assessment of the production requirements necessary to wage a major war across multiple theaters.\n**(2) Assessment**\nThe Commission shall assess the following:\n**(A)**\nLessons learned from the experience of major war in Ukraine, including a classified annex addressed to whether current operational plans for major war contingency scenarios in Europe, the Middle East, and Asia give due consideration to the lessons learned from that and other recent conflicts around the world.\n**(B)**\nThe expected defense production requirements necessary to wage a major war across one or more theaters, with attention to minimum production requirements, ordinary production requirements, and requirements in order to scale production quickly and at need.\n**(C)**\nIdentification and establishment of minimum and optimal production and stocks of key, critical weapons systems and associated munitions production and maintenance capacity indexed against operational planning for major war in Europe, the Middle East, and Asia.\n**(D)**\nThe current, standing capacity of the United States defense industrial base to produce weapons systems, ammunition, and other necessary supplies and maintenance necessary for different major war contingency scenarios, including sub-tier contracting, with a view to identifying supply chain bottlenecks, obstacles to competition, and requirements for the conversion of civilian commercial facilities to defense production in a national emergency.\n**(E)**\nThe policies and programs of the Federal Government that affect domestic industrial capacity that is or can be used for defense production.\n**(F)**\nThe burden imposed on different sectors within the defense industrial base as a result of regulations issued by\u2014\n**(i)**\nthe Department of Energy;\n**(ii)**\nthe Environmental Protection Agency;\n**(iii)**\nthe Department of Commerce;\n**(iv)**\nthe Department of Defense; and\n**(v)**\nthe Small Business Administration.\n**(3) Recommendations**\nThe Commission shall make recommendations with respect to the following matters:\n**(A)**\nReforms to operational planning and defense procurement planning with a view to ensuring United States contingency plans\u2014\n**(i)**\nare well suited to likely contingency scenarios;\n**(ii)**\nreflect the lessons learned from recent wars to include Russia\u2019s war in Ukraine; and\n**(iii)**\nreflect the correct balance of new and legacy technology to provide the United States the greatest possible operational advantage in future contingency operations.\n**(B)**\nReforms to existing Federal programs and policies related to defense production, procurement, and innovation.\n**(C)**\nFederal regulations that inhibit defense production and innovation and their estimated burden to producers, including regulations issued by\u2014\n**(i)**\nthe Department of Energy;\n**(ii)**\nthe Environmental Protection Agency;\n**(iii)**\nthe Department of Commerce; and\n**(iv)**\nthe Department of Defense.\n**(D)**\nFunding levels necessary to support increased domestic industrial capacity.\n**(E)**\nNew Federal policies, programs, and offices that can support a defense-industrial mobilization and increased domestic industrial capacity.\n##### (e) Report and briefing required\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, the Commission shall submit to the President and the appropriate congressional committees a report on the Commission\u2019s findings, conclusions, and recommendations.\n**(2) Elements**\nThe report required under paragraph (1) shall include\u2014\n**(A)**\na proposed strategy for increasing the industrial capacity of the United States for defense production;\n**(B)**\nthe assessment required by subsection (d)(2);\n**(C)**\nthe recommendations required by subsection (d)(3); and\n**(D)**\nconsiderations for policymakers, including members and committees of Congress.\n**(3) Interim briefing**\nNot later than 180 days after the deadline for appointment of members of the Commission specified in subsection (c)(3)(A), the Commission shall provide to the appropriate congressional committees a briefing on the status of the review, assessments, and recommendations required by subsection (d), including a discussion of any interim recommendations.\n##### (f) Advice and input\nThe Committee shall seek the advice and input of industry partners, manufacturing policy experts, State and local development officials, and manufacturing worker interests when performing the duties described in subsection (d) and producing the report required under subsection (e), including by\u2014\n**(1)**\nholding not less than 4 public hearings per year during which industry representatives, worker groups, and regional representatives can provide insight regarding the current state of the defense-industrial base and the requirements for its full mobilization; and\n**(2)**\nestablishing an Industry Advisory Board of not more than 10 members appointed by the chair, which shall include\u2014\n**(A)**\nan expert in industrial competitiveness and national security;\n**(B)**\na manufacturing trade association representative;\n**(C)**\na representative of small business government contractors;\n**(D)**\na manufacturing worker representative;\n**(E)**\na representative from a private investment firm investing in the defense and industrial sectors; and\n**(F)**\nsuch other representatives as the chair may appoint.\n##### (g) Assistance from Federal agencies\n**(1) Information and suggestions**\nThe Commission may secure directly from the Department of Defense, the Department of Energy, the Department of Commerce, the Environmental Protection Agency, the Small Business Administration, the Department of the Treasury, and the United States Trade Representative information, suggestions, estimates, and statistics for the purposes of this section. Each such agency shall, to the extent authorized by law, furnish such information, suggestions, estimates, and statistics directly to the Commission upon receiving a request made by\u2014\n**(A)**\nthe chair of the Commission;\n**(B)**\nthe chair of any subcommittee of the Commission created by a majority of members of the Commission; or\n**(C)**\nany member the Commission designated by a majority of the Commission for purposes of making requests under this paragraph.\n**(2) Additional assistance**\nDepartments and agencies of the United States may provide to the Commission such services, funds, facilities, staff, and other support services as those departments and agencies may determine advisable and as may be authorized by law.\n##### (h) Compensation and travel expenses\n**(1) Status as federal employees**\nNotwithstanding the requirements of section 2105 of title 5, United States Code, including the requirements relating to supervision under subsection (a)(3) of such section, the members of the Commission shall be deemed to be Federal employees.\n**(2) Compensation**\nEach member of the Commission may be compensated at not to exceed the daily equivalent of the annual rate of basic pay in effect for a position at level IV of the Executive Schedule under section 5315 of title 5, United States Code, for each day during which that member is engaged in the actual performance of the duties of the Commission.\n**(3) Travel expenses**\nWhile away from their homes or regular places of business in the performance of services for the Commission, members of the Commission shall be allowed travel expenses, including per diem in lieu of subsistence, in the same manner as persons employed intermittently in the Government service are allowed expenses under section 5703 of title 5, United States Code.\n##### (i) Staff\n**(1) Executive director**\nThe Commission shall appoint and fix the rate of basic pay for an Executive Director in accordance with section 3161 of title 5, United States Code.\n**(2) Pay**\nThe Executive Director appointed under paragraph (1) may, with the approval of the Commission, appoint and fix the rate of basic pay for additional personnel as staff of the Commission in accordance with section 3161(d) of title 5, United States Code.\n##### (j) Personal services\n**(1) Authority to procure**\nThe Commission may\u2014\n**(A)**\nprocure the services of experts or consultants (or of organizations of experts or consultants) in accordance with the provisions of section 3109 of title 5, United States Code; and\n**(B)**\npay in connection with such services travel expenses of individuals, including transportation and per diem in lieu of subsistence, while such individuals are traveling from their homes or places of business to duty stations.\n**(2) Maximum daily pay rates**\nThe daily rate paid an expert or consultant procured pursuant to paragraph (1) may not exceed the daily equivalent of the annual rate of basic pay in effect for a position at level IV of the Executive Schedule under section 5315 of title 5, United States Code.\n##### (k) Contracting authority\nThe Commission may acquire administrative supplies and equipment for Commission use to the extent funds are available.\n##### (l) Authority To accept gifts\n**(1) In general**\nThe Commission may accept, sue, and dispose of gifts or donations of services, goods, and property from non-Federal entities for the purposes of aiding and facilitating the work of the Commission. The authority under this paragraph does not extend to gifts of money.\n**(2) Documentation; conflicts of interest**\nThe Commission shall document gifts accepted under the authority provided by paragraph (1) and shall avoid conflicts of interest or the appearance of conflicts of interest.\n**(3) Compliance with congressional ethics rules**\nExcept as specifically provided in this section, a member of the Commission shall comply with rules set forth by the Select Committee on Ethics of the Senate and the Committee on Ethics of the House of Representative governing employees of the Senate and the House of Representatives, respectively.\n##### (m) Postal services\nThe Commission may use the United States mails in the same manner and under the same conditions as departments and agencies of the United States.\n##### (n) Commission support\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Defense shall seek to enter into a contract with a federally funded research and development center to provide appropriate staff and administrative support for the activities of the Commission.\n##### (o) Expedition of security clearances\nThe Office of Senate Security and the Office of House Security shall ensure the expedited processing of appropriate security clearances for personnel appointed to the Commission by offices of the Senate and House of Representatives, respectively, under processes developed for the clearance of legislative branch employees.\n##### (p) Legislative advisory committee\nThe Commission shall operate as a legislative advisory committee and shall not be subject to the provisions of the Federal Advisory Committee Act (5 U.S.C. App.).\n##### (q) Funding\nThere is authorized to be appropriated $7,000,000 for the Commission to carry out activities under this Act. Such funds shall remain available until expended.\n##### (r) Termination\n**(1) In general**\nThe Commission shall terminate on the date that is 90 days after the Commission submits the final report required by subsection (e).\n**(2) Administrative actions before termination**\nThe Commission may use the 90-day period described in paragraph (1) for the purpose of concluding its activities, including providing testimony to committees of Congress with respect to and disseminating the report required by subsection (e).\n##### (s) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Armed Services of the Senate; and\n**(2)**\nthe Committee on Armed Services of the House of Representatives.",
      "versionDate": "2025-04-30",
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
        "updateDate": "2025-05-29T17:57:29Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1524is.xml"
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
      "title": "William S. Knudsen Defense Remobilization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "William S. Knudsen Defense Remobilization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the William S. Knudsen Commission for American Defense-Industrial Mobilization, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:50Z"
    }
  ]
}
```
