# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4012?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4012
- Title: Fiscal Commission Act
- Congress: 119
- Bill type: S
- Bill number: 4012
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-24T16:50:45Z
- Update date including text: 2026-03-24T16:50:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4012",
    "number": "4012",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Fiscal Commission Act",
    "type": "S",
    "updateDate": "2026-03-24T16:50:45Z",
    "updateDateIncludingText": "2026-03-24T16:50:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T19:12:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-05",
      "state": "ME"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "DE"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "IN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NH"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "LA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "ND"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4012is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4012\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Curtis (for himself, Mr. King , Mr. Tillis , Mr. Coons , Mr. Young , Mrs. Shaheen , Mr. Cassidy , Mr. Kaine , Mr. Cramer , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo establish a commission on fiscal responsibility and reform.\n#### 1. Short title\nThis Act may be cited as the Fiscal Commission Act .\n#### 2. Definitions\nIn this Act:\n**(1) Co-chair**\nThe term co-chair means an individual appointed to serve as a co-chair of the Fiscal Commission under section 3(a)(3)(B)(i).\n**(2) Direct spending**\nThe term direct spending has the meaning given that term in section 250(c) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 901(c) ).\n**(3) Discretionary appropriations**\nThe term discretionary appropriations has the meaning given that term in section 250(c) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 901(c) ).\n**(4) Fiscal Commission**\nThe term Fiscal Commission means the commission established under section 3(a)(1)(A).\n**(5) Implementing bill**\nThe term implementing bill means a bill or joint resolution consisting solely of the legislative text the Fiscal Commission approves in accordance with clauses (i) and (ii) of section 3(a)(2)(B) and submits under clause (v) of such section.\n**(6) Outside expert**\nThe term outside expert means an individual who is not an elected official or an officer or employee of the Federal Government or of any State.\n#### 3. Establishment of Fiscal Commission\n##### (a) Establishment of fiscal commission\n**(1) Establishment**\n**(A) In general**\nEffective on the date that is 60 days after the date of enactment of this Act, there is established in Congress a Fiscal Commission.\n**(B) Goals**\nThe goals of the Commission shall be to educate, and bring awareness to, the people of the United States about the fiscal path the Nation is on, including\u2014\n**(i)**\neducating the people of the United States so they understand the fiscal state of the Nation and the cost of not addressing such state; and\n**(ii)**\ninforming the people of the United States about the deterioration of the fiscal health of the Nation, and that the debt poses a significant risk to the long-term fiscal sustainability of the Nation, with implications for future generations.\n**(2) Duties**\n**(A) Improve fiscal condition**\n**(i) In general**\nThe Fiscal Commission shall identify policies to\u2014\n**(I)**\nmeaningfully improve the long-term fiscal condition of the Federal Government, including reducing the debt and deficit;\n**(II)**\nachieve a sustainable ratio of the public debt of the Federal Government to the gross domestic product of the United States, which shall be not more than 100 percent, by fiscal year 2039; and\n**(III)**\nimprove the solvency, for a period of at least 75 years, of trust funds used to carry out Federal programs.\n**(ii) Requirements**\nIn carrying out clause (i), the Fiscal Commission shall propose recommendations that meaningfully improve the long-term fiscal condition of the Federal Government, including\u2014\n**(I)**\nchanges to address the current levels of discretionary appropriations, direct spending, and revenues and the gap between current revenues and expenditures of the Federal Government; and\n**(II)**\nchanges to address the growth of discretionary appropriations, direct spending, and revenues and the gap between the projected revenues and expenditures of the Federal Government.\n**(iii) Recommendations of committees**\nNot later than 60 days after the date described in paragraph (1), each committee of the Senate and the House of Representatives may transmit to the Fiscal Commission any recommendations of the committee relating to changes in law to further the duties described in clause (i) or (ii).\n**(iv) Interim report**\nThe Fiscal Commission may meet to consider, and vote on, an interim report on\u2014\n**(I)**\nthe findings and recommendations of the Fiscal Commission regarding the budgetary effects of changes in economic output, employment, capital stock, and other macroeconomic variables resulting from public and private investments;\n**(II)**\nany findings or recommendations of the Fiscal Commission with respect to carrying out the goals described in paragraph (1)(B); and\n**(III)**\nas the Fiscal Commission determines appropriate, any findings resulting from any hearing held or evidence received by the Commission.\n**(B) Report identified policies**\n**(i) In general**\nSubject to paragraph (4)(D)(ii)(II), not earlier than November 4, 2026, and, subject to clause (vi), not later than November 13, 2026, the Fiscal Commission shall meet to consider, and vote on\u2014\n**(I)**\na report that contains\u2014\n**(aa)**\na detailed statement of\u2014\n(AA)\nthe findings and recommendations of the Fiscal Commission regarding the budgetary effects of changes in economic output, employment, capital stock, and other macroeconomic variables resulting from public and private investments;\n(BB)\nany findings or recommendations of the Fiscal Commission with respect to carrying out the goals described in paragraph (1)(B); and\n(CC)\nas the Fiscal Commission determines appropriate, any findings resulting from any hearing held or evidence received by the Commission;\n**(bb)**\na statement of the economic and budgetary effects of the legislative language described in subclause (II); and\n**(cc)**\nthe estimate of the Congressional Budget Office required under paragraph (4)(D)(ii); and\n**(II)**\nlegislative language to carry out the recommendations of the Fiscal Commission in the report described in subclause (I)(aa).\n**(ii) Approval of report and legislative language**\nA report and legislative language of the Fiscal Commission under clause (i) shall only be approved upon an affirmative vote of a majority of the voting members of the Fiscal Commission, including the affirmative vote of not less than 2 voting members who were appointed by members of the Republican Party and not less than 2 voting members who were appointed by members of the Democratic Party.\n**(iii) Additional views**\n**(I) In general**\nA member of the Fiscal Commission who gives notice of an intention to file supplemental, minority, or additional views at the time of the final Fiscal Commission vote on the approval of the report and legislative language of the Fiscal Commission under clause (i) shall be entitled to 3 days to file those views in writing with the staff director of the Fiscal Commission.\n**(II) Inclusion in report**\nViews filed under subclause (I) shall be included in the report of the Fiscal Commission under clause (i) and printed in the same volume, or part thereof, and such inclusion shall be noted on the cover of the report, except that, in the absence of timely notice, the report may be printed and transmitted immediately without such views.\n**(iv) Report and legislative language to be made public**\nUpon the approval or disapproval of a report and legislative language in accordance with clauses (i) and (ii) by the Fiscal Commission, the Fiscal Commission shall promptly, and not more than 24 hours after the approval or disapproval or, if timely notice is given under clause (iii), not more than 24 hours after additional views are filed under such clause, make the report, the legislative language, and a record of the vote on the report and legislative language available to the public.\n**(v) Submission of report and legislative language**\nIf a report and legislative language are approved by the Fiscal Commission in accordance with clauses (i) and (ii), not later than 3 days after the date on which the report and legislative language are made available to the public under clause (iv), the Fiscal Commission shall submit the report and legislative language to the President, the Vice President, the Speaker of the House of Representatives, and the majority and minority leaders of each House of Congress.\n**(vi) Extension**\nThe Fiscal Commission may extend the deadline set forth in clause (i) to April 13, 2027, if the Fiscal Commission determines that additional time is necessary to complete the duties of the Fiscal Commission under this Act. Such an extension shall only be approved upon an affirmative vote of a majority of the voting members of the Fiscal Commission, including the affirmative vote of not less than 2 voting members who were appointed by members of the Republican Party and not less than 2 voting members who were appointed by members of the Democratic Party.\n**(C) Public awareness campaign**\nNot later than 30 days after the date the Fiscal Commission submits the report under subparagraph (B)(v), the Fiscal Commission shall complete a national campaign to increase public awareness and education with respect to the fiscal condition of the Nation.\n**(3) Membership**\n**(A) In general**\nThe Fiscal Commission shall be composed of 16 members who shall be appointed, not later than 14 days after the date described in paragraph (1) and with due consideration to chairs and ranking minority members of the committees and subcommittees of subject matter jurisdiction (as applicable), as follows:\n**(i)**\nThe majority leader of the Senate shall appoint 3 members from among the Members of the Senate and 1 member who is an outside expert.\n**(ii)**\nThe minority leader of the Senate shall appoint 3 members from among the Members of the Senate and 1 member who is an outside expert.\n**(iii)**\nThe Speaker of the House of Representatives shall appoint 3 members from among the Members of the House of Representatives and 1 member who is an outside expert.\n**(iv)**\nThe minority leader of the House of Representatives shall appoint 3 members from among the Members of the House of Representatives and 1 member who is an outside expert.\n**(B) Co-chairs**\n**(i) In general**\nNot later than 14 days after the date described in paragraph (1)\u2014\n**(I)**\nthe leadership of the Senate and House of Representatives of the same political party as the President shall appoint 1 individual from among the members of the Fiscal Commission who shall serve as a co-chair of the Fiscal Commission; and\n**(II)**\nthe leadership of the Senate and House of Representatives of the opposite political party as the President shall appoint 1 individual from among the members of the Fiscal Commission who shall serve as a co-chair of the Fiscal Commission.\n**(ii) Staff director**\nThe co-chairs of the Fiscal Commission, acting jointly, shall appoint a staff director for the Fiscal Commission.\n**(C) Period of appointment**\n**(i) In general**\nThe members of the Fiscal Commission shall be appointed for the life of the Fiscal Commission.\n**(ii) Vacancy**\n**(I) In general**\nAny vacancy in the Fiscal Commission shall not affect the powers of the Fiscal Commission, but shall be filled not later than 14 days after the date on which the vacancy occurs, in the same manner as the original appointment was made.\n**(II) Ineligible members**\nIf a member of the Fiscal Commission who was appointed as a Member of the Senate or the House Representatives ceases to be a Member of the Senate or the House of Representatives, as applicable\u2014\n**(aa)**\nthe member shall no longer be a member of the Fiscal Commission; and\n**(bb)**\na vacancy in the Fiscal Commission exists.\n**(4) Administration**\n**(A) In general**\nTo enable the Fiscal Commission to exercise the powers, functions, and duties of the Fiscal Commission, there are authorized to be disbursed by the Secretary of the Senate from the accounts determined appropriate under section 5 the actual and necessary expenses of the Fiscal Commission approved by the co-chairs of the Fiscal Commission, subject to the rules and regulations of the Senate.\n**(B) Space for Fiscal Commission**\nNot later than 90 days after the date of enactment of this Act, the Architect of the Capitol, in consultation with the Fiscal Commission, shall identify suitable space to house the operations of the Fiscal Commission.\n**(C) Quorum**\nSeven voting members of the Fiscal Commission shall constitute a quorum for purposes of voting, meeting, and holding hearings. A member who is an outside expert shall not be counted for purposes of determining whether there is a quorum under this subparagraph.\n**(D) Voting**\n**(i) Proxy voting**\nNo proxy voting shall be allowed on behalf of any member of the Fiscal Commission.\n**(ii) Congressional budget office estimates**\n**(I) In general**\nThe Director of the Congressional Budget Office shall, with respect to the legislative language of the Fiscal Commission described in paragraph (2)(B)(i)(II), provide to the Fiscal Commission\u2014\n**(aa)**\nestimates of the legislative language in accordance with sections 308(a) and 201(f) of the Congressional Budget Act of 1974 ( 2 U.S.C. 639(a) , 601(f)); and\n**(bb)**\ninformation on the budgetary effects of the legislative language on the long-term fiscal outlook.\n**(II) Limitation**\nThe Fiscal Commission may not vote on any version of the report, recommendations, or legislative language of the Fiscal Commission under paragraph (2)(B)(i) unless the estimates and information described in subclause (I) of this clause are made available for consideration by all members of the Fiscal Commission not later than 48 hours before that vote, as certified by the co-chairs of the Fiscal Commission.\n**(iii) Outside experts nonvoting members**\nOnly members of the Fiscal Commission who are Members of the Senate or the House of Representatives may vote on any matter of the Fiscal Commission. An outside expert serving as a member of the Fiscal Commission shall be a nonvoting member.\n**(E) Meetings**\n**(i) Initial meeting**\nNot later than 45 days after the date described in paragraph (1), the Fiscal Commission shall hold the first meeting of the Fiscal Commission.\n**(ii) Agenda**\nThe co-chairs of the Fiscal Commission shall provide an agenda to the members of the Fiscal Commission not later than 48 hours before each meeting of the Fiscal Commission.\n**(F) Hearings**\n**(i) In general**\nThe Fiscal Commission may, for the purpose of carrying out this section, hold such hearings, sit and act at such times and places, require attendance of witnesses and production of books, papers, and documents, take such testimony, receive such evidence, and administer such oaths as the Fiscal Commission considers advisable.\n**(ii) Hearing procedures and responsibilities of co-chairs**\n**(I) Announcement**\nThe co-chairs of the Fiscal Commission shall make a public announcement of the date, place, time, and subject matter of any hearing to be conducted under this subparagraph not later than 7 days before the date of the hearing, unless the co-chairs determine that there is good cause to begin such hearing on an earlier date.\n**(II) Written statement**\nA witness appearing before the Fiscal Commission shall file a written statement of the proposed testimony of the witness not later than 2 days before the date of the appearance of the witness, unless the co-chairs of the Fiscal Commission\u2014\n**(aa)**\ndetermine that there is good cause for the witness to not file the written statement; and\n**(bb)**\nwaive the requirement that the witness file the written statement.\n**(iii) Hearing requirements**\nThe Fiscal Commission shall hold not less than 6 hearings under this subparagraph, which shall include\u2014\n**(I)**\nfield hearings throughout the Nation;\n**(II)**\nhearings to solicit testimony from appropriate officers and employees of the executive branch; and\n**(III)**\nhearings to solicit testimony from Members of the Senate or the House of Representatives, Delegates to the House of Representatives, and the Resident Commissioner from Puerto Rico.\n**(G) Technical assistance and consultation**\nUpon written request of the co-chairs of the Fiscal Commission, the head of a Federal agency (including a legislative branch agency) shall provide technical assistance to, and consult with, the Fiscal Commission in order for the Fiscal Commission to carry out its duties.\n**(H) Outside expert**\nAny outside expert appointed to the Fiscal Commission\u2014\n**(i)**\nshall not be considered to be a Federal employee for any purpose by reason of service on the Fiscal Commission; and\n**(ii)**\nshall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the Commission.\n##### (b) Staff of Fiscal Commission\n**(1) In general**\nThe co-chairs of the Fiscal Commission may jointly appoint and fix the compensation of staff of the Fiscal Commission as the co-chairs determine necessary, in accordance with the guidelines, rules, and requirements relating to employees of the Senate.\n**(2) Pay**\nThe pay of each employee of the Fiscal Commission shall be disbursed by the Secretary of the Senate.\n##### (c) Ethical standards\n**(1) Members**\nA member of the Fiscal Commission appointed by a Member of the Senate and any employee of the Fiscal Commission shall adhere to the ethics rules of the Senate.\n**(2) House of representatives**\nA member of the Fiscal Commission appointed by a Member of the House of Representatives shall adhere to the ethics rules and requirements of the House of Representatives.\n##### (d) Termination\nThe Fiscal Commission shall terminate on the earlier of\u2014\n**(1)**\nthe date that is 30 days after the date the Fiscal Commission submits the report under subsection (a)(2)(B)(v); or\n**(2)**\nMay 17, 2027.\n#### 4. Expedited consideration of implementing bills\n##### (a) Qualifying legislation\nOnly an implementing bill shall be entitled to expedited consideration under this section.\n##### (b) Consideration in the House of Representatives\n**(1) Introduction**\nIf the Fiscal Commission approves legislative language in accordance with clauses (i) and (ii) of section 3(a)(2)(B) and submits the legislative language in accordance with clause (v) of such section, the implementing bill consisting solely of that legislative language shall be introduced in the House of Representatives (by request)\u2014\n**(A)**\nby the majority leader of the House of Representatives, or by a Member of the House of Representatives designated by the majority leader of the House of Representatives, on the third legislative day after the date the Fiscal Commission approves and submits such legislative language; or\n**(B)**\nif the implementing bill is not introduced under subparagraph (A), by any Member of the House of Representatives on any legislative day beginning on the legislative day after the legislative day described in subparagraph (A).\n**(2) Referral and reporting**\nAny committee of the House of Representatives to which an implementing bill is referred shall report the implementing bill to the House of Representatives without amendment not later than 5 legislative days after the date on which the implementing bill was so referred. If any committee of the House of Representatives to which an implementing bill is referred fails to report the implementing bill within that period, that committee shall be automatically discharged from consideration of the implementing bill, and the implementing bill shall be placed on the appropriate calendar.\n**(3) Proceeding to consideration**\nAfter the last committee authorized to consider an implementing bill reports it to the House of Representatives or has been discharged from its consideration, it shall be in order to move to proceed to consider the implementing bill in the House of Representatives. Such a motion shall not be in order after the House of Representatives has disposed of a motion to proceed with respect to the implementing bill. The previous question shall be considered as ordered on the motion to its adoption without intervening motion.\n**(4) Consideration**\nThe implementing bill shall be considered as read. All points of order against the implementing bill and against its consideration are waived. The previous question shall be considered as ordered on the implementing bill to its passage without intervening motion except 2 hours of debate equally divided and controlled by the proponent and an opponent.\n**(5) Vote on passage**\nThe vote on passage of the implementing bill shall occur pursuant to the constraints under clause 8 of rule XX of the Rules of the House of Representatives.\n##### (c) Expedited procedure in the Senate\n**(1) Introduction in the Senate**\nOn the day on which an implementing bill is submitted to the Senate under section 3(a)(2)(B)(v), the implementing bill shall be introduced, by request, by the majority leader of the Senate for himself or herself and the minority leader of the Senate, or by any Member so designated by them. If the Senate is not in session on the day on which such implementing bill is submitted, it shall be introduced as provided on the first day thereafter on which the Senate is in session. Such implementing bill shall be placed on the Calendar of Business under General Orders.\n**(2) Proceeding**\nNotwithstanding rule XXII of the Standing Rules of the Senate, it is in order, not later than 2 days of session after the date on which an implementing bill is placed on the Calendar, for the majority leader of the Senate or the designee of the majority leader to move to proceed to the consideration of the implementing bill. It shall also be in order for any Member of the Senate to move to proceed to the consideration of the implementing bill at any time after the conclusion of such 2-day period. A motion to proceed is in order even though a previous motion to the same effect has been disagreed to. All points of order against the motion to proceed to the implementing bill are waived. The motion to proceed is not debatable. The motion is not subject to a motion to postpone. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order. If a motion to proceed to the consideration of the implementing bill is agreed to, it shall remain the unfinished business until disposed of. All points of order against the implementing bill and against its consideration are waived.\n**(3) No amendments**\nAn amendment to the implementing bill, a motion to postpone, a motion to proceed to the consideration of other business, or a motion to commit the implementing bill is not in order.\n**(4) Rulings of the chair on procedure**\nAppeals from the decisions of the Chair relating to the application of the rules of the Senate, as the case may be, to the procedure relating to an implementing bill shall be decided without debate.\n##### (d) Amendment\nAn implementing bill shall not be subject to amendment in either the Senate or the House of Representatives.\n##### (e) Consideration by the other House\n**(1) In general**\nIf, before passing an implementing bill, one House receives from the other House an implementing bill\u2014\n**(A)**\nthe implementing bill of the other House shall not be referred to a committee; and\n**(B)**\nthe procedure in the receiving House shall be the same as if no implementing bill had been received from the other House until the vote on passage, when the implementing bill received from the other House shall supplant the implementing bill of the receiving House.\n**(2) Revenue measures**\nThis subsection shall not apply to the House of Representatives if an implementing bill received from the Senate is a revenue measure.\n##### (f) Rules To coordinate action with other house\n**(1) Treatment of implementing bill of other House**\nIf an implementing bill is not introduced in the Senate or the Senate fails to consider an implementing bill under this section, the implementing bill of the House of Representatives shall be entitled to expedited floor procedures under this section.\n**(2) Treatment of companion measures in the Senate**\nIf, following passage of an implementing bill in the Senate, the Senate then receives from the House of Representatives an implementing bill, the House-passed implementing bill shall not be debatable. The vote on passage of the implementing bill in the Senate shall be considered to be the vote on passage of the implementing bill received from the House of Representatives.\n**(3) Vetoes**\nIf the President vetoes an implementing bill, consideration of a veto message in the Senate under this paragraph shall be 10 hours equally divided between the majority and minority leaders of the Senate or the designees of the majority and minority leaders of the Senate.\n#### 5. Funding\nFunding for the Fiscal Commission shall be derived from such accounts of the Senate as are determined appropriate by the Committee on Appropriations of the Senate.\n#### 6. Rulemaking\nThe provisions of section 4 are enacted by Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and, as such, the provisions\u2014\n**(A)**\nshall be considered as part of the rules of each House, respectively, or of that House to which they specifically apply; and\n**(B)**\nshall supersede other rules only to the extent that they are inconsistent therewith; and\n**(2)**\nwith full recognition of the constitutional right of either House to change such rules (so far as relating to such House) at any time, in the same manner, and to the same extent as in the case of any other rule of such House.",
      "versionDate": "2026-03-05",
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
        "name": "Congress",
        "updateDate": "2026-03-24T16:50:44Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4012is.xml"
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
      "title": "Fiscal Commission Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fiscal Commission Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a commission on fiscal responsibility and reform.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:18:34Z"
    }
  ]
}
```
