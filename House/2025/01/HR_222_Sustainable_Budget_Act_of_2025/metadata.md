# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/222?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/222
- Title: Sustainable Budget Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 222
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2026-04-30T08:06:59Z
- Update date including text: 2026-04-30T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-07 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-07 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/222",
    "number": "222",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Sustainable Budget Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:59Z",
    "updateDateIncludingText": "2026-04-30T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-07T16:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "AR"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "IA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "NE"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "GA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "PA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr222ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 222\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Mr. Case (for himself, Mr. Womack , Mr. Peters , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on the Budget , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a national commission on fiscal responsibility and reform, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sustainable Budget Act of 2025 .\n#### 2. Establishment of Commission\n##### (a) Establishment\nNot later than 30 days after the date of the enactment of this Act, there shall be established within the legislative branch a commission to be known as the National Commission on Fiscal Responsibility and Reform (referred to in this Act as the Commission ).\n##### (b) Membership\n**(1) Composition of Commission**\nA Commission shall be composed of 18 members of whom\u2014\n**(A)**\nsix members shall be appointed by the President, of whom not more than 4 shall be from the same political party;\n**(B)**\nthree members shall be appointed by the majority leader of the Senate, from among current Members of the Senate;\n**(C)**\nthree members shall be appointed by the Speaker of the House of Representatives, from among current Members of the House of Representatives;\n**(D)**\nthree members shall be appointed by the minority leader of the Senate, from among current Members of the Senate; and\n**(E)**\nthree members shall be appointed by the minority leader of the House of Representatives, from among current Members of the House of Representatives.\n**(2) Initial appointments**\nInitial appointments to the Commission shall be made not later than 60 days after the establishment of the Commission.\n**(3) Vacancy**\nA vacancy on the Commission shall be filled in the same manner as the initial appointment.\n##### (c) Co-Chairpersons\nFrom among the members appointed under paragraph (1), the President shall designate 2 members, who shall not be of the same political party, to serve as Co-Chairpersons of the Commission.\n##### (d) Qualifications\nMembers appointed to the Commission shall have significant depth of experience and responsibilities in matters relating to government service, fiscal policy, economics, Federal agency management or private sector management, public administration, and law.\n##### (e) Duties\n**(1) In general**\nThe Commission shall identify policies to improve the fiscal situation in the medium term and to achieve fiscal sustainability over the long term.\n**(2) Requirements**\nIn carrying out paragraph (1), the Commission shall\u2014\n**(A)**\npropose recommendations designed to balance the budget, excluding interest payments on the debt, by the end of the 10-year period beginning on the date on which the Commission is established, in order to stabilize the debt-to-GDP ratio at an acceptable level; and\n**(B)**\npropose recommendations that meaningfully improve the long-term fiscal outlook, including changes to address the growth of entitlement spending and the gap between the projected revenues and expenditures of the Federal Government.\n##### (f) Reports\n**(1) In general**\n**(A) Final report**\nNot later than 1 year after the date on which members are appointed to the Commission under subsection (b), the Commission shall vote on the approval of a final report containing the recommendations required under subsection (e).\n**(B) Interim reports**\nAt any time after the date on which members are appointed and prior to voting on the approval of a final report under subparagraph (A), the Commission may vote on the approval of an interim report containing such recommendations described in subsection (e) as the Commission may provide.\n**(2) Approval of report**\nThe Commission may only issue a report under this subsection if\u2014\n**(A)**\nthe report is approved by not less than 12 members of the Commission; and\n**(B)**\nof the members approving the report, at least 4 are members of the same political party to which the Speaker of the House of Representatives belongs and at least 4 are members of the same political party to which the minority leader of the House of Representatives belongs.\n**(3) Submission of report to congress**\nEach report approved under this subsection shall be submitted to Congress and made available to the public.\n##### (g) Powers of the commission\n**(1) Hearings**\nThe Commission may hold such hearings, sit and act at such times and places, take such testimony, and receive such evidence as the Commission considers advisable to carry out the duties of the Commission described in subsection (e).\n**(2) Information from Federal agencies**\nThe Commission may secure directly from any Federal agency such information as the Commission considers necessary to carry out the duties of the Commission described in subsection (e). Upon request from the Co-Chairpersons of the Commission, the head of the Federal agency shall provide the information requested to the Commission.\n**(3) Postal services**\nThe Commission may use the United States mail in the same manner and under the same conditions as other departments and agencies of the Federal Government.\n**(4) Website**\n**(A) Contents**\nThe Commission shall establish a website that shall contain\u2014\n**(i)**\nthe recommendations required under subsection (e); and\n**(ii)**\nthe records of attendance of the members of the Commission for each meeting of the Commission.\n**(B) Date of publication**\nThe Commission shall publish a recommendation or record of attendance described under subparagraph (A) on the website established under such subparagraph not later than 72 hours after the conclusion of the meeting at which such recommendation is made or at which such record of attendance is taken.\n##### (h) Assistance of other legislative branch entities\n**(1) Government Accountability Office**\nThe Comptroller General shall provide technical assistance to the Commission, as the Commission conducts the work of the Commission, on the findings and recommendations of the Government Accountability Office.\n**(2) Congressional Budget Office**\nThe Director of the Congressional Budget Office shall provide technical assistance to the Commission, as the Commission conducts the work of the Commission, on the findings and recommendations of the Congressional Budget Office.\n**(3) Joint Committee on Taxation**\nThe chair of the Joint Committee on Taxation shall provide technical assistance to the Commission, as the Commission conducts the work of the Commission, on the findings and recommendations of the Joint Committee on Taxation.\n##### (i) Personnel matters\n**(1) In general**\nMembers of the Commission shall serve without any additional compensation.\n**(2) Travel expenses**\nMembers of the Commission shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the Commission.\n**(3) Staff**\n**(A) In general**\nThe Co-Chairpersons of the Commission, may without regard to the civil service laws and regulations, appoint and terminate an executive director and such other additional personnel as may be necessary to enable the Commission to perform its duties. The employment of an executive director shall be subject to confirmation by the Commission.\n**(B) Compensation**\nThe Co-Chair\u00adper\u00adsons of the Commission may fix the compensation of the executive director and other personnel without regard to the provisions of chapter 51 and subchapter III of chapter 53 of title 5, United States Code, relating to the classification of positions and General Schedule pay rates, except that the rate of pay for the executive director and other personnel may not exceed the rate payable for level V of the Executive Schedule under section 5613 of such title.\n**(4) Detail of government employees**\nAny Federal Government employee may be detailed to the Commission without reimbursement, and such detail shall be without interruption or loss of civil service status or privilege.\n**(5) Procurement of temporary and intermittent services**\nThe Co-Chairpersons of each Commission may procure temporary and intermittent services under section 3109(b) of title 5, United States Code, at rates for individuals which do not exceed the daily equivalent of the annual rate of basic pay prescribed for level V of the Executive Schedule under section 5316 of such title.\n##### (j) Termination of the commission\nThe Commission established shall terminate 30 days after the date on which the Commission submits the final report of the Commission under subsection (f).\n##### (k) Rules of construction\nNothing in this Act shall be construed to\u2014\n**(1)**\nimpair or otherwise affect\u2014\n**(A)**\nauthority granted by law to an executive department, agency, or the head thereof; or\n**(B)**\nfunctions of the Director of the Office of Management and Budget relating to budgetary, administrative, or legislative proposals; or\n**(2)**\ncreate any right or benefit, substantive or procedural, enforceable at law or in equity by any party against the United States, its departments, agencies, or entities, its officers, employees, or agents, or any other person.\n##### (l) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to the Commission such sums as may be necessary to carry out this Act.\n**(2) Availability**\nAny sums appropriated under paragraph (1) shall remain available, without fiscal year limitation, until expended.\n##### (m) Federal agency defined\nThe term Federal agency means an establishment in the executive, legislative, or judicial branch of the Federal Government.\n#### 3. Consideration of commission recommendations\n##### (a) Submission of proposed joint resolution\nNot later than 60 days after the date on which the Commission submits a report to Congress under section 2(f)(3), the President shall transmit to Congress a special message on the report, accompanied by a proposed joint resolution consisting of legislative language to implement the recommendations contained in such report.\n##### (b) Requirements for preparation of proposed joint resolution\n**(1) Consultation with Congress**\n**(A) In general**\nThe President may not transmit a proposed joint resolution under subsection (a) until after the President completes consultation with Congress in accordance with this paragraph.\n**(B) Consultation with committees**\nThe President shall consult with the chairman and ranking minority member of each relevant committee of the Senate or of the House of Representatives regarding the contents of a proposed joint resolution.\n**(C) Requirements for consultation**\nThe consultation required under subparagraph (B) shall provide the opportunity for the chairman and ranking member of each relevant committee of the Senate or of the House of Representatives to provide\u2014\n**(i)**\nrecommendations for alternative means of addressing the recommendations contained in the Commission report; and\n**(ii)**\nrecommendations regarding which recommendations contained in the Commission report should not be addressed in the proposed joint resolution.\n**(D) Relevant committees**\nThe relevant committees of the Senate and the House of Representatives for purposes of this paragraph shall be\u2014\n**(i)**\ndetermined by the President; and\n**(ii)**\nbased on the content of the proposed joint resolution.\n**(2) Consultation with GAO and CBO**\nThe President shall prepare a proposed joint resolution transmitted under subsection (a) in consultation with the Comptroller General of the United States and the Director of the Congressional Budget Office.\n##### (c) Contents of special message\nA special message transmitted under subsection (a) shall\u2014\n**(1)**\nspecify recommendations outlined in the Commission report that are excluded from the proposed joint resolution;\n**(2)**\ndetail why the recommendations described in paragraph (1) were excluded from the proposed joint resolution;\n**(3)**\nspecify recommendations outlined in the Commission report that are included in the proposed joint resolution; and\n**(4)**\nidentify programs included in the Commission report that should be eliminated or consolidated.\n##### (d) Transmittal\nThe President shall submit the special message to the Secretary of the Senate if the Senate is not in session and to the Clerk of the House of Representatives if the House is not in session.\n##### (e) Public availability\nThe President shall make a copy of the special message and the proposed joint resolution publicly available, including publicly available on a website of the President, and shall publish in the Federal Register a notice of the message and information on how it can be obtained.\n#### 4. Expedited consideration of proposed joint resolution\n##### (a) Qualifying legislation\n**(1) In general**\nOnly a Commission joint resolution shall be entitled to expedited consideration under this section.\n**(2) Definition**\nIn this section, the term Commission joint resolution means a joint resolution which consists solely of the text of the proposed joint resolution submitted by the President under section 3(a).\n##### (b) Consideration in the House of Representatives\n**(1) Introduction**\nA Commission joint resolution may be introduced in the House of Representatives (by request)\u2014\n**(A)**\nby the majority leader of the House of Representatives, or by a Member of the House of Representatives designated by the majority leader of the House of Representatives, on the next legislative day after the date on which the President submits the proposed joint resolution under section 3(a); or\n**(B)**\nif the Commission joint resolution is not introduced under subparagraph (A), by any Member of the House of Representatives on any legislative day beginning on the legislative day after the legislative day described in subparagraph (A).\n**(2) Referral and reporting**\nAny committee of the House of Representatives to which a Commission joint resolution is referred shall report the Commission joint resolution to the House of Representatives without amendment not later than 10 legislative days after the date on which the Commission joint resolution was so referred. If a committee of the House of Representatives fails to report a Commission joint resolution within that period, it shall be in order to move that the House of Representatives discharge the committee from further consideration of the Commission joint resolution. Such a motion shall not be in order after the last committee authorized to consider the Commission joint resolution reports it to the House of Representatives or after the House of Representatives has disposed of a motion to discharge the Commission joint resolution. The previous question shall be considered as ordered on the motion to its adoption without intervening motion except 20 minutes of debate equally divided and controlled by the proponent and an opponent. If such a motion is adopted, the House of Representatives shall proceed immediately to consider the Commission joint resolution in accordance with paragraphs (3) and (4). A motion to reconsider the vote by which the motion is disposed of shall not be in order.\n**(3) Proceeding to consideration**\nAfter the last committee authorized to consider a Commission joint resolution reports it to the House of Representatives or has been discharged (other than by motion) from its consideration, it shall be in order to move to proceed to consider the Commission joint resolution in the House of Representatives. Such a motion shall not be in order after the House of Representatives has disposed of a motion to proceed with respect to the Commission joint resolution. The previous question shall be considered as ordered on the motion to its adoption without intervening motion. A motion to reconsider the vote by which the motion is disposed of shall not be in order.\n**(4) Consideration**\nThe Commission joint resolution shall be considered as read. All points of order against the Commission joint resolution and against its consideration are waived. The previous question shall be considered as ordered on the Commission joint resolution to its passage without intervening motion except 2 hours of debate equally divided and controlled by the proponent and an opponent and 1 motion to limit debate on the Commission joint resolution. A motion to reconsider the vote on passage of the Commission joint resolution shall not be in order.\n**(5) Vote on passage**\nThe vote on passage of the Commission joint resolution shall occur not later than 3 legislative days after the date on which the last committee authorized to consider the Commission joint resolution reports it to the House of Representatives or is discharged.\n##### (c) Expedited procedure in the Senate\n**(1) Introduction in the Senate**\nA Commission joint resolution may be introduced in the Senate (by request)\u2014\n**(A)**\nby the majority leader of the Senate, or by a Member of the Senate designated by the majority leader of the Senate, on the next legislative day after the date on which the President submits the proposed joint resolution under section 3(a); or\n**(B)**\nif the Commission joint resolution is not introduced under subparagraph (A), by any Member of the Senate on any day on which the Senate is in session beginning on the day after the day described in subparagraph (A).\n**(2) Committee consideration**\nA Commission joint resolution introduced in the Senate under paragraph (1) shall be jointly referred to the committee or committees of jurisdiction, which committees shall report the Commission joint resolution without any revision and with a favorable recommendation, an unfavorable recommendation, or without recommendation, not later than 10 session days after the date on which the Commission joint resolution was so referred. If any committee to which a Commission joint resolution is referred fails to report the Commission joint resolution within that period, that committee shall be automatically discharged from consideration of the Commission joint resolution, and the Commission joint resolution shall be placed on the appropriate calendar.\n**(3) Proceeding**\nNotwithstanding rule XXII of the Standing Rules of the Senate, it is in order, not later than 2 days of session after the date on which a Commission joint resolution is reported or discharged from all committees to which the Commission joint resolution was referred, for the majority leader of the Senate or the designee of the majority leader to move to proceed to the consideration of the Commission joint resolution. It shall also be in order for any Member of the Senate to move to proceed to the consideration of the Commission joint resolution at any time after the conclusion of such 2-day period. A motion to proceed is in order even though a previous motion to the same effect has been disagreed to. All points of order against the motion to proceed to the Commission joint resolution are waived. The motion to proceed is not debatable. The motion is not subject to a motion to postpone. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order. If a motion to proceed to the consideration of the Commission joint resolution is agreed to, the Commission joint resolution shall remain the unfinished business until disposed of. All points of order against a Commission joint resolution and against consideration of the Commission joint resolution are waived.\n**(4) No amendments**\nAn amendment to a Commission joint resolution, or a motion to postpone, or a motion to proceed to the consideration of other business, or a motion to recommit the Commission joint resolution, is not in order.\n**(5) Rulings of the Chair on procedure**\nAppeals from the decisions of the Chair relating to the application of the rules of the Senate, as the case may be, to the procedure relating to a Commission joint resolution shall be decided without debate.\n##### (d) Amendment\nA Commission joint resolution shall not be subject to amendment in either the Senate or the House of Representatives.\n##### (e) Consideration by the other House\n**(1) In general**\nIf, before passing a Commission joint resolution, a House receives from the other House a Commission joint resolution of the other House\u2014\n**(A)**\nthe Commission joint resolution of the other House shall not be referred to a committee; and\n**(B)**\nthe procedure in the receiving House shall be the same as if no Commission joint resolution had been received from the other House until the vote on passage, when the Commission joint resolution received from the other House shall supplant the Commission joint resolution of the receiving House.\n**(2) Revenue measures**\nThis subsection shall not apply to the House of Representatives if a Commission joint resolution received from the Senate is a revenue measure.\n##### (f) Rules To coordinate action with other House\n**(1) Treatment of Commission joint resolution of other House**\nIf a Commission joint resolution is not introduced in the Senate or the Senate fails to consider a Commission joint resolution under this section, the Commission joint resolution of the House of Representatives shall be entitled to expedited floor procedures under this section.\n**(2) Treatment of companion measures in the Senate**\nIf, following passage of a Commission joint resolution in the Senate, the Senate then receives from the House of Representatives a Commission joint resolution, the House-passed Commission joint resolution shall not be debatable. The vote on passage of the Commission joint resolution in the Senate shall be considered to be the vote on passage of the Commission joint resolution received from the House of Representatives.\n**(3) Vetoes**\nIf the President vetoes a Commission joint resolution, consideration of a veto message in the Senate under this paragraph shall be 10 hours equally divided between the majority and minority leaders of the Senate or the designees of the majority and minority leaders of the Senate.\n##### (g) Exercise of rulemaking power\nThis section is enacted by Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the Senate and House of Representatives, respectively, and as such it is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House in the case of a Commission joint resolution, and it supersedes other rules only to the extent that it is inconsistent with such rules; and\n**(2)**\nwith full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.",
      "versionDate": "2025-01-07",
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
            "name": "Advisory bodies",
            "updateDate": "2025-03-05T16:03:30Z"
          },
          {
            "name": "Budget deficits and national debt",
            "updateDate": "2025-03-05T16:03:30Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-03-05T16:03:30Z"
          },
          {
            "name": "Congressional operations and organization",
            "updateDate": "2025-03-05T16:03:30Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-05T16:03:30Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-05T16:03:30Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-03-05T16:03:30Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-03-05T16:03:30Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-03-05T16:03:30Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-03-05T16:03:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-02-27T13:43:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr222",
          "measure-number": "222",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr222v00",
            "update-date": "2025-02-27"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sustainable Budget Act of 2025</strong></p><p>This bill establishes the National Commission on Fiscal Responsibility and Reform within the legislative branch to identify policies to improve the fiscal situation in the medium term and achieve fiscal sustainability over the long term.</p><p>The commission must propose recommendations that (1) are designed to balance the budget, excluding interest payments on the debt, within 10 years; and (2) meaningfully improve the long-term fiscal outlook, including changes to address the growth of entitlement spending and the gap between projected federal revenues and expenditures.</p><p>Congress must consider the commission's recommendations using specified expedited legislative procedures.</p>"
        },
        "title": "Sustainable Budget Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr222.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sustainable Budget Act of 2025</strong></p><p>This bill establishes the National Commission on Fiscal Responsibility and Reform within the legislative branch to identify policies to improve the fiscal situation in the medium term and achieve fiscal sustainability over the long term.</p><p>The commission must propose recommendations that (1) are designed to balance the budget, excluding interest payments on the debt, within 10 years; and (2) meaningfully improve the long-term fiscal outlook, including changes to address the growth of entitlement spending and the gap between projected federal revenues and expenditures.</p><p>Congress must consider the commission's recommendations using specified expedited legislative procedures.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr222"
    },
    "title": "Sustainable Budget Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sustainable Budget Act of 2025</strong></p><p>This bill establishes the National Commission on Fiscal Responsibility and Reform within the legislative branch to identify policies to improve the fiscal situation in the medium term and achieve fiscal sustainability over the long term.</p><p>The commission must propose recommendations that (1) are designed to balance the budget, excluding interest payments on the debt, within 10 years; and (2) meaningfully improve the long-term fiscal outlook, including changes to address the growth of entitlement spending and the gap between projected federal revenues and expenditures.</p><p>Congress must consider the commission's recommendations using specified expedited legislative procedures.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr222"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr222ih.xml"
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
      "title": "Sustainable Budget Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sustainable Budget Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a national commission on fiscal responsibility and reform, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:18:15Z"
    }
  ]
}
```
