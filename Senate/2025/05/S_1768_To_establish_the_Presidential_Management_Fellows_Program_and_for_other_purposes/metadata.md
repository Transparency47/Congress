# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1768?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1768
- Title: TALENTS Act
- Congress: 119
- Bill type: S
- Bill number: 1768
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2026-04-23T00:03:21Z
- Update date including text: 2026-04-23T00:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1768",
    "number": "1768",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "TALENTS Act",
    "type": "S",
    "updateDate": "2026-04-23T00:03:21Z",
    "updateDateIncludingText": "2026-04-23T00:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T21:32:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1768is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1768\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Kim (for himself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish the Presidential Management Fellows Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Training Aspiring Leaders Emerging Now To Serve Act or the TALENTS Act .\n#### 2. Definitions\nIn this Act:\n**(1) Advanced degree; qualifying educational institution**\n**(A) In general**\nThe terms advanced degree and qualifying educational institution have the meanings given those terms in section 362.102 of title 5, Code of Federal Regulations, or any successor regulation.\n**(B) Determination by Director**\nThe Director may determine whether a master\u2019s certificate qualifies as an advanced degree for the purposes of the Program.\n**(2) Agency**\nThe term agency \u2014\n**(A)**\nhas the meaning given the term Executive agency in section 105 of title 5, United States Code; and\n**(B)**\nincludes the Government Publishing Office.\n**(3) Agency PMF Coordinator**\nThe term agency PMF Coordinator means an individual, at the appropriate component level of an agency, who\u2014\n**(A)**\ncoordinates the placement, development, and other Program-related activities of Fellows appointed in the agency; and\n**(B)**\nsatisfies the criteria described in section 362.104(a)(8) of title 5, Code of Federal Regulations, or any successor regulation.\n**(4) Director**\nThe term Director means the Director of the Office of Personnel Management.\n**(5) Executive Resources Board**\nThe term Executive Resources Board \u2014\n**(A)**\nmeans an Executive Resources Board described in section 317.501(a) of title 5, Code of Federal Regulations, or any successor regulation; and\n**(B)**\nwith respect to an agency that is not required to have an Executive Resources Board pursuant to section 317.501(a) of title 5, Code of Federal Regulations, or any successor regulation, means the senior agency official to whom the head of the agency has given responsibility for executive resources management and oversight.\n**(6) Federal Executive Board**\nThe term Federal Executive Board means a Federal Executive Board established under section 11.\n**(7) Fellow**\nThe term Fellow means an individual appointed to serve as a Fellow under the Program.\n**(8) Metropolitan area**\nThe term metropolitan area means a geographic zone surrounding a major city, as defined and delimited from time to time by the Director.\n**(9) Principal area officer**\n**(A) In general**\nThe term principal area officer means, with respect to an agency, the senior official of the agency who is located in a metropolitan area and who has no superior official within that metropolitan area other than in the regional office of the agency.\n**(B) Multiple bureaus**\nIf an agency maintains facilities of more than 1 bureau or other subdivision within a metropolitan area, and the heads of those facilities are in separate chains of command within the agency, the agency may have more than 1 principal area officer.\n**(10) Principal regional officer**\nThe term principal regional officer means, with respect to an agency, the senior official in a regional office of the agency.\n**(11) Program**\nThe term Program means the Presidential Management Fellows Program established under this Act.\n**(12) Special representative**\nThe term special representative means, with respect to an agency, an official who is\u2014\n**(A)**\nnot subject to the supervision of a principal regional officer or a principal area officer; and\n**(B)**\nspecifically designated by the head of the agency to serve as the personal representative of the head of the agency.\n#### 3. Program establishment and administration\n##### (a) Establishment\nThere is established the Presidential Management Fellows Program, the purpose of which is to attract to the Federal service outstanding individuals from a variety of academic disciplines and career paths who have a clear interest in, and commitment to, excellence in the leadership and management of public policies and programs.\n##### (b) Director responsibilities\n**(1) Number of Fellows**\n**(A) In general**\nSubject to subparagraph (B), the Director shall determine the number of individuals who will be finalists to be appointed as Fellows during any given fiscal year, which shall be based on input from the Chief Human Capital Officers Council and from agencies not represented on that Council.\n**(B) Increase in positions during fiscal years 2026 through 2031**\nDuring each of fiscal years 2026 through 2031, the Director shall ensure that the number of positions for Fellows under the Program during the applicable fiscal year is equal to 200 percent of the number of positions for Fellows under the Program in the fiscal year preceding the fiscal year in which this Act is enacted, as the Program was carried out under subpart D of part 362 of title 5, Code of Federal Regulations, as in effect during that fiscal year.\n**(2) Establishment of qualifications**\nThe Director shall establish the qualification requirements for evaluating applicants for the Program.\n##### (c) Agency processes\n**(1) In general**\nAfter the Director makes the determination under subsection (b)(1)(A) with respect to a fiscal year, an agency may appoint individuals selected by the Director as finalists to be Fellows according to the short-, medium-, and long-term senior leadership and related recruitment, development, and succession requirements of the agency.\n**(2) Field locations outside of Washington, DC**\nAn agency that appoints a Fellow to a position in a field location outside of the Washington, DC metropolitan area may\u2014\n**(A)**\nbefore making the appointment, discuss whether the candidate would like to do a developmental rotation to the headquarters of the agency and, if so, make a commitment to allow and fund such a rotation, to the maximum extent practicable, in accordance with section 6(b); and\n**(B)**\npromote interaction among regional Fellows with the agency Federal Executive Board and permit that Fellow to attend activities sanctioned by that Federal Executive Board in that region.\n#### 4. Announcement, eligibility, and selection\n##### (a) Announcement\nThe Director shall annually announce the ability to apply for the Program and conduct a competition for the selection of finalists, as set forth in this section.\n##### (b) Eligibility\n**(1) Application period**\nTo apply for participation in the Program, an individual shall\u2014\n**(A)**\nhave obtained an advanced degree from a qualifying educational institution not more than 2 years before the date on which the Director makes the applicable announcement under subsection (a); or\n**(B)**\nif the individual is attending a graduate or professional school (such as law school or medical school), as of the date on which the individual applies, expect to complete an advanced degree described in subparagraph (A) not later than August 31 of the academic year in which the competition is held.\n**(2) Service as Fellow**\nAn individual may not serve as a Fellow unless the individual has, not more than 2 years before the date on which the individual begins serving as a Fellow, completed an advanced degree from a qualifying educational institution.\n**(3) Multiple applications**\nAn individual may apply to participate in the Program more than once if the individual satisfies the applicable eligibility criteria, except that, if an individual becomes a finalist and subsequently applies to participate in the Program during the next open announcement, the individual shall forfeit that status of the individual as a finalist.\n##### (c) Selection\n**(1) In general**\nThe Director shall select Fellow finalists based on the results of a rigorous structured assessment process, which shall allow the Director to grant a preference for any individual who is preference eligible, as defined in section 2108 of title 5, United States Code, in accordance with the provisions of that title.\n**(2) Publication of list**\nThe Director shall publish and provide to agencies a list of Fellow finalists.\n#### 5. Appointment and extension\n##### (a) Appointments\n**(1) In general**\nAn agency\u2014\n**(A)**\nmay, subject to subsection (b), make 2-year appointments to the Program under Schedule D of the excepted service in accordance with part 302 of title 5, Code of Federal Regulations, or any successor regulations; and\n**(B)**\nshall appoint a Fellow using the excepted service appointing authority provided under section 213.3402(c) of title 5, Code of Federal Regulations, or any successor regulation.\n**(2) Eligibility period**\nThe Director shall establish an eligibility period during which agencies may appoint Fellow finalists.\n##### (b) Extensions\nIn accordance with criteria established by an agency, the agency may extend the term of a Fellow for not more than 120 days to cover a rare or unusual circumstance.\n##### (c) Grade\nAn agency may appoint a Fellow at the GS\u201309, GS\u201311, or GS\u201312 level (or any equivalent under a pay and classification system other than the General Schedule, such as the Federal Wage System) depending on the qualifications of the Fellow.\n##### (d) Trial period\nThe duration of the appointment of a Fellow in the excepted service shall be considered to be a trial period, but not a probationary period.\n##### (e) Work schedules\n**(1) In general**\nSubject to the other provisions of this subsection, a Fellow shall have a full-time work schedule.\n**(2) Part-time schedules**\n**(A) In general**\nA Fellow may request a part-time work schedule for a limited period of not more than 180 days, which the agency may approve if\u2014\n**(i)**\nthe agency and the Fellow have determined that such approval would not negatively impact the ability of the Fellow to meet all Program requirements by the end of the appointment of the Fellow; and\n**(ii)**\nthe agency includes an approval of a specific time period during which the part-time work schedule applies that the agency determines to be appropriate.\n**(B) Updating of agreement**\nThe Program agreement of a Fellow shall be updated with the new work schedule of the Fellow upon the approval of any part-time schedule under subparagraph (A).\n**(C) Rule of construction**\nNothing in this paragraph may be construed to entitle a Fellow to the approval of a request for a part-time work schedule.\n##### (f) Relationship to direct-Hire authority\nNotwithstanding any provision of section 3115 or 3116 of title 5, United States Code, an appointment by an agency under the Program shall be considered to be an appointment made using the authority provided to the agency under the applicable section.\n#### 6. Development, evaluation, promotion, and certification\n##### (a) Individual Development Plans\nNot later than 90 days after the date on which the Program begins in a fiscal year, the head of each agency shall approve an Individual Development Plan (referred to in this section as an IDP ) for each Fellow serving under an appointment within the agency, which shall\u2014\n**(1)**\nset forth the specific developmental activities that are mutually agreed upon by the Fellow and the supervisor of the Fellow; and\n**(2)**\nbe developed in consultation with\u2014\n**(A)**\nthe supervisor of the Fellow; and\n**(B)**\n**(i)**\nthe agency PMF Coordinator; or\n**(ii)**\nthe mentor assigned to the Fellow, who shall not be required to be assigned by the agency.\n##### (b) Required developmental activities\n**(1) General resources**\n**(A) OPM responsibilities**\nThe Director shall provide, for each class or cohort of Fellows\u2014\n**(i)**\nleadership development activities and general Program resources; and\n**(ii)**\ninformation on available training opportunities known to the Director.\n**(B) Agency responsibilities**\nEach agency shall provide to each class or cohort of Fellows appropriate agency-specific onboarding and employee orientation activities.\n**(2) Agency training**\n**(A) In general**\nEach agency shall provide each Fellow serving under an appointment within the agency not fewer than 80 hours of formal interactive training per year that addresses the competencies outlined in the applicable IDP.\n**(B) Certain training not included**\nMandatory annual training, such as information security and ethics training, shall not count toward the satisfaction of the requirement under subparagraph (A).\n**(3) Mentors**\nNot later than 90 days after the start of an appointment of a Fellow, the applicable agency shall assign the Fellow a mentor, who shall be a managerial employee of the agency outside the chain of command of the Fellow.\n**(4) Assignments**\nAn agency shall provide each Fellow serving under an appointment within the agency with not less than 1 rotational or developmental assignment with full-time management or technical responsibilities that is consistent with the IDP of the Fellow and the following:\n**(A)**\nEach Fellow shall receive not less than 1 developmental assignment that is not shorter than 120 days and not longer than 180 days, which shall have management or technical responsibilities consistent with the IDP of the Fellow.\n**(B)**\n**(i)**\nThe developmental assignment described in subparagraph (A) may be within the organization of the Fellow, in another component of the employing agency, or in another agency, as permitted by the employing agency.\n**(ii)**\nEach assignment described in this subparagraph shall be in a different work unit led by a supervisor other than the usual supervisor of the Fellow.\n**(C)**\n**(i)**\nEach developmental assignment described in subparagraph (A) shall provide a challenging work experience of a caliber appropriate for a participant in the flagship leadership development program of the Federal Government.\n**(ii)**\nFor the purposes of clause (i), an appropriate developmental assignment may include a project implementing a new executive order or major piece of legislation, agency reorganization, or cross-agency collaboration on a major initiative.\n**(5) Short-term assignments**\nIn addition to the assignments described in paragraph (4), a Fellow may receive another short-term rotational assignment, which\u2014\n**(A)**\nshall be not shorter than 30 days and not longer than 180 days, at the discretion of the employing agency; and\n**(B)**\nmay take place within the organization of the Fellow, in another component of the employing agency, or in another agency, as permitted by the employing agency.\n**(6) Assessment of subsequent classes**\n**(A) In general**\nUpon the request of the Director, the employing agency shall make a Fellow available to assist in the assessment process for subsequent Program classes.\n**(B) Satisfaction of training requirements**\nAny interactive training provided to a Fellow in connection with assisting the Director under subparagraph (A) may be counted toward the training requirement under paragraph (2).\n##### (c) Promotion\n**(1) In general**\nAn employing agency may promote any Fellow who meets the qualification requirements for the applicable position.\n**(2) Rule of construction**\nNothing in paragraph (1) may be construed to confer any entitlement to a promotion.\n##### (d) Certificate of completion\n**(1) In general**\n**(A) ERB evaluation**\nNot later than 45 days before the date on which the Program ends in a fiscal year, each Executive Resources Board shall evaluate each Fellow serving under an appointment within the applicable agency and determine whether the Executive Resources Board can certify in writing that the Fellow met all of the requirements of the Program, including the performance and developmental expectations set forth in the performance plan and IDP of the Fellow.\n**(B) Consultation permitted**\nIn carrying out subparagraph (A), an Executive Resources Board may consult with the mentor of a Fellow.\n**(2) Successful completion**\n**(A) Notification**\nNot later than 30 days before the date on which a Fellow completes the Program, an Executive Resources Board shall notify each Fellow serving under an appointment within the applicable agency regarding the decision of the Board with respect to certification of successful completion of the Program by the Fellow.\n**(B) Conversion eligibility**\nA Fellow who the applicable Executive Resources Board certifies as having met all of the requirements of the Program shall be eligible for conversion in accordance with section 10.\n**(C) Forwarding to OPM**\nEach Executive Resources Board shall forward to the Director all certifications of the Board under this paragraph.\n**(3) Failure to certify**\n**(A) In general**\nIf an Executive Resources Board decides not to certify a Fellow under this subsection, the Fellow may request reconsideration of that determination by the Director, if the Fellow, not later than 15 days after the date on which the Board makes that decision, submits the request in writing with appropriate documentation and justification.\n**(B) Continuation in Program**\nWith respect to a Fellow who has submitted a request for reconsideration under subparagraph (A)\u2014\n**(i)**\nthe Fellow may continue in the Program pending the outcome of that request; and\n**(ii)**\nthe applicable agency shall continue to provide appropriate developmental activities to the Fellow during the period in which that request is pending.\n**(C) Ineligibility**\nA Fellow who is not approved for certification under this subsection and who has not submitted a timely request for reconsideration under subparagraph (A), or whose request for reconsideration under that subparagraph (A) has been denied, shall not be eligible for conversion under section 10.\n#### 7. Movement between agencies\n##### (a) In general\nAt any time during the appointment of a Fellow, the Fellow may move to another agency, if\u2014\n**(1)**\nthe receiving agency meets all the requirements for participating in the Program;\n**(2)**\nthe original agency releases the appointment of the Fellow to the receiving agency; and\n**(3)**\nthe new employing agency appoints the Fellow without a break in service.\n##### (b) Terms of service\nUpon appointment by a new employing agency under subsection (a)(3)\u2014\n**(1)**\nthe Fellow shall not begin a new Program period; and\n**(2)**\nbecause there is no break in service, the time served by the Fellow under the previous Program appointment shall apply towards the completion of the Program with the new employing agency.\n##### (c) Notification required\nAn agency shall notify the Director upon making an appointment described in subsection (a)(3).\n##### (d) Reimbursements\nIf a move under this section occurs during the first 180 days of the appointment of a Fellow, the initial employing agency may request from the new appointing agency reimbursement of 1/4 of the placement fee with respect to the Fellow.\n#### 8. Withdrawal and readmission\n##### (a) Withdrawal\n**(1) In general**\n**(A) Treatment of withdrawal**\nA Fellow may withdraw from the Program at any time, which shall be treated as a resignation from the Federal service, except that any obligations established upon appointment, such as from accepting a recruitment incentive under part 575 of title 5, Code of Federal Regulations, or any successor regulations, shall still apply.\n**(B) Notification**\nAn agency shall notify the Director when a Fellow within the agency withdraws from the Program.\n**(2) Competitive service**\n**(A) In general**\nA Fellow who held a permanent appointment in the competitive service in an agency immediately before entering the Program, and who withdraws from the Program for a reason that is not related to misconduct, poor performance, or suitability, may, at the discretion of the employing agency, be placed in a permanent competitive service position, as appropriate, in that agency.\n**(B) Not subject to appeal**\nThe determination of an agency under subparagraph (A) shall not be subject to appeal.\n##### (b) Readmission\n**(1) No readmission**\nIf a Fellow withdraws from the Program for a reason that relates to misconduct, poor performance, or suitability, as determined by the employing agency, the individual may not be readmitted to the Program at any time.\n**(2) Petition**\n**(A) In general**\nIf a Fellow withdraws from the Program for a reason that is not related to misconduct, poor performance, or suitability, the individual may petition the original employing agency for readmission and reappointment to the Program.\n**(B) Requirements**\nA petition submitted under subparagraph (A) shall be in writing and include the appropriate justification for the requested readmission and reappointment, and the applicable agency may approve or deny the request.\n**(C) Submission to OPM**\nIf, under subparagraph (B), an agency approves a petition submitted under subparagraph (A), the agency shall submit that approved petition to the Director, which shall include the status of the applicable individual in the Program upon readmission and reappointment.\n**(D) OPM discretion**\nThe Director, upon receipt of an approved petition under subparagraph (C), may overrule the decision of the agency submitting that approved petition, and that decision of the Director shall not be subject to appeal.\n#### 9. Removal and reduction in force\n##### (a) Removal\n**(1) In general**\nAn agency may remove a Fellow for a reason related to misconduct, poor performance, or suitability, upon which the agency shall submit to the Director written notification of the removal.\n**(2) End of term**\n**(A) In general**\nAs a condition of employment, the appointment of a Fellow shall end at the end of the 2-year Program period, plus any agency-approved extension of the appointment of the Fellow under section 5(b), unless the Fellow is converted under section 10.\n**(B) Failure to convert**\nIf an agency does not convert a Fellow at the end of the Program, as provided in section 10, or extend the appointment of the Fellow under section 5(b), the appointment of the Fellow shall expire on the date that is 30 days after the date on which, as applicable\u2014\n**(i)**\nthe certification for Program completion is denied under section 6(d)(3); or\n**(ii)**\nthe Director denies a request submitted by an agency for an extension of the appointment.\n##### (b) Reduction in force\nEach Fellow shall be in the excepted service group II for purposes of section 351.502 of title 5, Code of Federal Regulations, or any successor regulation.\n#### 10. Conversion to the competitive service\n##### (a) In general\nA Fellow shall complete the Program within the time limits established under section 5, including any agency-approved extension under that section, after which the Fellow may be converted under subsection (b).\n##### (b) Conversion\nAn agency may convert, without a break in service, a Fellow who has been successfully certified under section 6(d)(2) to a term or permanent position in the competitive service for which the Fellow is qualified.\n##### (c) Conversion at A different agency\nA Fellow may be converted under subsection (b) to a position at a different agency if the following conditions are satisfied:\n**(1)**\nThe original employing agency is unable to convert the Fellow to a position in the competitive service in the organizational unit of the agency in which the Fellow has served or another component within the agency\u2014\n**(A)**\nincluding because of unforeseen budget constraints, a reorganization, the abolishment of positions, or any other appropriate reason; and\n**(B)**\nwhich is not because of the failure of the Fellow to obtain a certification under section 6(d)(2) or because of the misconduct, poor performance, or suitability of the Fellow.\n**(2)**\nThe conversion shall occur before the end of the Program period, as established under section 5, plus any agency-approved extension under that section.\n**(3)**\nThe position at the new agency shall have a full performance level that is equivalent to, or less than, the position to which the Fellow would have been converted at the original employing agency.\n#### 11. Federal Executive Boards\n##### (a) Authority and status\nThere are established Federal Executive Boards\u2014\n**(1)**\nto strengthen the management and administration of executive branch activities in selected centers of field operations; and\n**(2)**\nwhich are organized and function under the authority of the Director.\n##### (b) Locations\n**(1) In general**\nFederal Executive Boards are established, or shall continue, as applicable, in the following metropolitan areas:\n**(A)**\nAlbuquerque-Santa Fe.\n**(B)**\nAtlanta.\n**(C)**\nBaltimore.\n**(D)**\nBoston.\n**(E)**\nBuffalo.\n**(F)**\nChicago.\n**(G)**\nCincinnati.\n**(H)**\nCleveland.\n**(I)**\nDallas-Fort Worth.\n**(J)**\nDenver.\n**(K)**\nDetroit.\n**(L)**\nHonolulu.\n**(M)**\nHouston.\n**(N)**\nKansas City.\n**(O)**\nLos Angeles.\n**(P)**\nMiami.\n**(Q)**\nMinneapolis-St. Paul.\n**(R)**\nNew Orleans.\n**(S)**\nNew York.\n**(T)**\nNewark.\n**(U)**\nPhiladelphia.\n**(V)**\nPittsburgh.\n**(W)**\nPortland.\n**(X)**\nSt. Louis.\n**(Y)**\nSan Francisco.\n**(Z)**\nSeattle.\n**(2) Action by Director**\nThe Director may dissolve, merge, or divide any of the Federal Executive Boards described in paragraph (1), or establish new Federal Executive Boards, as the Director determines to be necessary, proper, or convenient.\n##### (c) Membership\n**(1) Presidential directive**\nThe President shall direct the head of each agency to arrange for the leading officials of the field activities of the agency to participate personally in the work of Federal Executive Boards.\n**(2) Members**\n**(A) In general**\nThe head of each agency shall designate\u2014\n**(i)**\nby title of office, the principal regional officer, if any, and the principal area officer, if any, who shall represent the agency on each Federal Executive Board; and\n**(ii)**\nby name and title of office, the special representative, if any, who shall represent the head of the agency on each Federal Executive Board.\n**(B) Designations**\nA designation made under subparagraph (A)\u2014\n**(i)**\nshall be made in writing and transmitted to the Director;\n**(ii)**\nmay be transmitted through the Chair of a Federal Executive Board; and\n**(iii)**\nmay be amended at any time by the head of the applicable agency.\n**(3) Alternate members**\n**(A) In general**\nEach member of a Federal Executive Board may designate any alternate member, who shall attend meetings and otherwise serve in the absence of the member.\n**(B) Status**\nAn alternate member shall be the deputy or principal assistant to the member or another senior official of the organization of the member.\n##### (d) Officers and organization\n**(1) Bylaws**\n**(A) In general**\nEach Federal Executive Board shall adopt bylaws or other rules for the internal governance of the Board, subject to the approval of the Director.\n**(B) Contents**\nThe bylaws described in subparagraph (A), and other rules of a Federal Executive Board, may reflect the particular needs, resources, and customs of the Board, if those bylaws and rules are not inconsistent with this section or the directives of the President or the Director.\n**(C) Conflicts**\nIf bylaws or rules described in subparagraph (B) conflict with this section or the directives of the President or the Director, those bylaws or rules, as applicable, shall have no force or effect.\n**(2) Chair**\nEach Federal Executive Board shall have a Chair, who shall be elected by the members of the Board and who shall serve for a term of office of not more than 1 year.\n**(3) Staff**\n**(A) In general**\nAs the members of a Federal Executive Board determine necessary and proper, those members shall designate personnel from the respective organizations of the members to serve as the staff, or otherwise to participate in, the activities of the Board.\n**(B) Other staff**\nAdditional personnel beyond the personnel described in subparagraph (A) may be engaged, by appointment, contract, or otherwise, only with the approval of the Director.\n**(4) Termination**\n**(A) In general**\nUnless otherwise expressly provided by law, by directive of the President or the Director, or by the bylaws of the applicable Federal Executive Board, each committee, subcommittee, council, and other subunit of the Board, and each affiliation of the Board with external organizations, shall terminate upon expiration of the term of office of the Chair of the Board.\n**(B) Reestablishment**\nA committee, subcommittee, council, other subunit, or affiliation of a Federal Executive Board may be reestablished or renewed by affirmative action of the Board.\n**(5) Board actions**\n**(A) In general**\nA Federal Executive Board may take an action only with the approval of a majority of the members of the Board.\n**(B) No delegation permitted**\nThe authority under subparagraph (A) may not be delegated.\n**(C) Conformance with law**\nEach activity of a Federal Executive Board shall conform to applicable laws and reflect prudent uses of official time and funds.\n##### (e) OPM leadership\n**(1) Role of Director**\nThe Director\u2014\n**(A)**\nshall be responsible to the President for the organizational and programmatic activities of the Federal Executive Boards;\n**(B)**\ndirect and oversee the activities of the Federal Executive Boards consistent with law and the directives of the President; and\n**(C)**\nmay consult with, and require the advice of, the Chair, members, or staff of a Federal Executive Board.\n**(2) Role of regional representatives**\nThe Chair of each Federal Executive Board shall report to the Director through the regional representative of the Director and the regional representative of the Director shall oversee the activities of, and periodically visit and meet with, the Federal Executive Boards.\n**(3) Communications**\n**(A) In general**\nThe Director shall maintain channels of communication\u2014\n**(i)**\nfrom the Director through the regional representatives of the Director to the Chairs of the Federal Executive Boards; and\n**(ii)**\nbetween and among the Federal Executive Boards through the Director and the regional representatives of the Director.\n**(B) Use of channels**\nAny agency may use the channels described in subparagraph (A) to communicate with the Director and with the Federal Executive Boards.\n**(C) Communications by Chairs**\nThe Chair of a Federal Executive Board may communicate with the Director on recommendations for action at the national level, on significant management problems that cannot be addressed at the local level, and on other matters of interest to the executive branch.\n**(4) Reports**\n**(A) In general**\nEach Federal Executive Board shall transmit to the Director, over the signature of the Chair of the Board, an annual work plan and an annual report to the Director on the significant programs and activities of the Board in each fiscal year, which shall\u2014\n**(i)**\nwith respect to each such work plan\u2014\n**(I)**\nset forth the proposed general agenda for the succeeding fiscal year;\n**(II)**\nbe submitted on or before July 1; and\n**(III)**\nbe subject to the approval of the Director; and\n**(ii)**\nwith respect to each such annual report\u2014\n**(I)**\ndescribe and evaluate the activities of the preceding fiscal year; and\n**(II)**\nbe submitted on or before January 1.\n**(B) Other reports**\nIn addition to the requirements under subparagraph (A), members of each Federal Executive Board shall keep the headquarters of the respective agency informed of the activities of the Board by timely reports through appropriate agency channels.\n**(5) Conferences**\nThe Director may convene regional and national conferences of the Chairs and other representatives of Federal Executive Boards.\n##### (f) Authorized activities\n**(1) In general**\nEach Federal Executive Board shall\u2014\n**(A)**\nserve as an instrument of outreach for the national headquarters of the executive branch to executive branch activities in the applicable metropolitan area;\n**(B)**\nconsider common management and program problems and develop cooperative agreements that will promote the general objectives of the Federal Government and of the several agencies in the applicable metropolitan area, which shall be made with the guidance and approval of the Director, within the range of the delegated authority and discretion held by members, alternates, and staff in that area, consistent with the missions of the agencies involved;\n**(C)**\nprovide a forum for the exchange of information between Washington, DC and the field, and among field elements in the applicable metropolitan area, about programs, management methods, and problems;\n**(D)**\ndevelop local coordinated approaches to the development and operation of programs that have common characteristics;\n**(E)**\ncommunicate management initiatives and other concerns from Washington, DC to the field to achieve better mutual understanding and support;\n**(F)**\nrefer problems that cannot be solved locally to the national level; and\n**(G)**\nsubject to the guidance of the Director, be responsible for\u2014\n**(i)**\npresidential initiatives on management reforms;\n**(ii)**\npersonnel initiatives of the Office of Personnel Management;\n**(iii)**\nprograms led by the Office of Management and Budget;\n**(iv)**\nfacilities planning led by the General Services Administration;\n**(v)**\nthe local Combined Federal Campaign, under the direction of the Director;\n**(vi)**\nthe sharing of technical knowledge and resources in finance, internal auditing, personnel management, automated data processing applications, interagency use of computer installations, and similar commonly beneficial activities;\n**(vii)**\nthe pooling of resources to provide, as efficiently as possible, and at the least possible cost to the taxpayers of the United States, common services, such as employee first-aid, cardiopulmonary resuscitation (referred to in this clause as CPR ), CPR training, preventative health programs, assistance to the aging, blood donor programs, and savings bond drives;\n**(viii)**\nthe encouragement of employee initiative and better performance through special recognition and other incentive programs;\n**(ix)**\nthe provision of assistance in the implementation and upgrading of performance management systems;\n**(x)**\nemergency operations, such as under hazardous weather conditions, responding to blood donation needs, and communicating related leave policies;\n**(xi)**\nthe recognition of the service of veterans and the dissemination of information relating to programs and benefits available to veterans in the Federal service; and\n**(xii)**\nsuch other programs, projects, and operations as may be set forth in the annual work plan approved by the Director.\n**(2) Advisory role**\nThe Director\u2014\n**(A)**\nshall advise the Federal Executive Boards on activities in the areas of performance appraisal and incentives, interagency training programs, the educational development of employees of agencies, improvement of labor-management relations, equal employment opportunity (including related programs of the Federal Government), and selective placement programs for handicapped individuals; and\n**(B)**\nmay direct a Federal Executive Board to address such specific programs, or undertake such cooperative activities, as the Director determines necessary or proper.\n##### (g) Additional rules and directives\nThe Director may issue further rules and guidance for, and directives to, the Federal Executive Boards.\n#### 12. Reports\nNot later than 3 years after the date of enactment of this Act, and not less frequently than once every 3 years thereafter, the Director shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives a report that addresses the Program, which shall include an analysis of any structural challenges facing the Program and recommendations on measures to strengthen the Program.",
      "versionDate": "2025-05-14",
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
        "actionDate": "2025-12-12",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "6700",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TALENTS Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-04T17:05:09Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1768is.xml"
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
      "title": "TALENTS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TALENTS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Training Aspiring Leaders Emerging Now To Serve Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Presidential Management Fellows Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:16Z"
    }
  ]
}
```
