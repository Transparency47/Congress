# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7894?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7894
- Title: Truman Scholarship Clean House Act
- Congress: 119
- Bill type: HR
- Bill number: 7894
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-04-02T18:44:17Z
- Update date including text: 2026-04-02T18:44:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 13.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 13.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7894",
    "number": "7894",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001196",
        "district": "21",
        "firstName": "Elise",
        "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
        "lastName": "Stefanik",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Truman Scholarship Clean House Act",
    "type": "HR",
    "updateDate": "2026-04-02T18:44:17Z",
    "updateDateIncludingText": "2026-04-02T18:44:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 13.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
        "item": [
          {
            "date": "2026-03-17T19:26:56Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-12T13:31:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7894ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7894\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Ms. Stefanik introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo make improvements to the Harry S Truman Memorial Scholarship Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Truman Scholarship Clean House Act .\n#### 2. Definitions\nSection 3 of the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2002 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) through (6) as paragraphs (2) through (7), respectively; and\n**(2)**\nby inserting before paragraph (2), as so redesignated, the following:\n(1) affiliated with , when used with respect to an individual\u2019s relationship to a certain political party, means that the individual\u2014 (A) is a registered member of that political party; (B) is a current or former holder of elected public office from that political party; (C) is a current or former candidate for public office from that political party; (D) is a current or former political appointee associated with that political party; (E) is a current staffer of\u2014 (i) a holder of elected public office from that political party; (ii) a candidate of that political party; or (iii) a fundraising organization for such members or candidates; or (F) is a current or former judicial appointee nominated or otherwise selected by a holder of elected public office from that political party. .\n#### 3. Harry S Truman Scholarship Foundation\n##### (a) Board of Trustees\nSection 5 of the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2004 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking The Board shall be composed of and all that follows through the end of subparagraph (D); and\n**(B)**\nby adding at the end the following:\n(2) The Board shall be composed of 13 members, as follows: (A) One member appointed by the Speaker of the House of Representatives. (B) One member appointed by the minority leader of the House of Representatives. (C) One member appointed by the majority leader of the Senate. (D) One member appointed by the minority leader of the Senate. (E) Eight members, not more than four of whom may be affiliated with the same political party at the time of appointment, to be appointed by the President with the advice and consent of the Senate. (F) The Secretary of Education or the Secretary\u2019s designee, who shall serve ex officio as a member of the Board, but shall not be eligible to serve as Chairperson. ;\n**(2)**\nby amending subsection (c) to read as follows:\n(c) (1) Except as provided in paragraph (2), the term of office of each member of the Board (other than Secretary of Education or the Secretary\u2019s designee serving ex officio) shall be six years. (2) As designated by the President at the time of appointment, of the members first appointed under subsection (b)(2)(E) after the date of enactment of this paragraph\u2014 (A) three shall be appointed for terms of two years; (B) three shall be appointed for terms of four years; and (C) two shall be appointed for terms of six years. (3) Any member of the Board appointed to fill a vacancy shall serve for the remainder of the term for which the member\u2019s predecessor was appointed, and shall be appointed in the same manner as the original appointment for that vacancy was made. (4) No member of the Board (other than the Secretary of Education or the Secretary\u2019s designee serving ex officio) may serve more than two six-year terms, regardless of whether the terms are consecutive. A member described in subparagraph (A) or (B) of paragraph (2) who serves an initial term of less than six years, may serve up to two additional six-year terms following the expiration of such member\u2019s initial term. ; and\n**(3)**\nby adding at the end the following:\n(e) Seven members of the Board shall constitute a quorum. .\n##### (b) Transition and Implementation\n**(1) Dissolution of existing Board of Trustees**\nEffective on the date that is 90 days after the date of enactment of this Act, the Board of Trustees of the Harry S Truman Scholarship Foundation (as established under section 5 of the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2004 )) is dissolved and all members of the Board are terminated.\n**(2) Appointment of new members**\nAs soon as practicable after the effective date specified in paragraph (1), new members shall be appointed to the Board of Trustees of the Harry S Truman Scholarship Foundation in accordance with section 5 of the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2004 ), as amended by subsection (a).\n#### 4. Selection of Truman Scholars\nSection 7 of the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2006 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby inserting the eligibility requirements described in subsection (c) and before minimum criteria ; and\n**(B)**\nby inserting in accordance with subsection (d)(4) before the period at the end;\n**(2)**\nby adding at the end the following:\n(c) A student is eligible to be nominated for a scholarship under this Act if such student\u2014 (1) is\u2014 (A) a full-time undergraduate student enrolled at an institution of higher education who will receive a bachelor\u2019s degree in the academic year following the academic year in which the student is applying for a scholarship; or (B) a full-time senior level student from the Commonwealth of Puerto Rico or from The Islands (as defined in section 1801.2(b) of title 45, Code of Federal Regulations (as in effect on the date of the enactment of this subsection)); (2) is enrolled in a course of study that qualifies the student for admission to a graduate program leading to a career in public service; (3) has a demonstrated record of academic excellence; and (4) is a citizen or national of the United States or a permanent resident of the Commonwealth of the Northern Mariana Islands. (d) (1) The Foundation shall establish and maintain Regional Review Panels for purposes of carrying out subsection (a). (2) Each Regional Review Panel shall be responsible for selecting scholarship recipients from one or more States assigned to the Panel by the Board. (3) (A) Each Regional Review Panel shall consist of not fewer than five members, each of whom shall be appointed on an annual basis by an affirmative vote of not less than two-thirds of the members of the Board. (B) Not more than half of the members of a Regional Review Panel may be affiliated with the same political party at the time of appointment. (4) In selecting students to be scholarship recipients under this Act, each Regional Review Panel\u2014 (A) shall select students based on\u2014 (i) the extent and quality of community service and government involvement of the student; (ii) the leadership record of the student; (iii) the academic performance of the student, including with respect to and writing and analytical skills; and (iv) the suitability and appropriateness of the student\u2019s proposed graduate program of study for a career in public service; (B) shall not select any student who\u2014 (i) served as a leader, officer, director, or organizer of a student organization recognized by the institution of higher education at which the student is enrolled at time of an incident or conduct that led to the suspension or expulsion of such organization from such institution; (ii) has been suspended or expelled by an institution of higher education due to a violation of such institution\u2019s code of conduct or other disciplinary action by such institution; or (iii) has been convicted by any Federal, State, or local court of competent jurisdiction of a felony; and (C) may not disfavor or otherwise apply adverse considerations to a student because the student intends to pursue a particular type of graduate degree, including with respect to a Master of Business Administration degree or Doctor of Medicine degree. .\n#### 5. Termination of scholarship\nSection 9 of the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2008 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting in accordance with subsection (c) and after provided in this Act ; and\n**(2)**\nby adding at the end the following:\n(c) (1) In accordance with paragraph (2), a student awarded a scholarship under the provisions of this Act may not continue to receive the payments provided in this Act if, at any point after the date on which the scholarship is received, the student\u2014 (A) with respect to a report or request required by the Foundation\u2014 (i) fails to submit such a report or request; or (ii) provides false, misleading, or materially incomplete information on any such report or request; (B) fails to begin use of the scholarship within four years of the date of receipt of a bachelor\u2019s degree, unless granted an extension in writing by the Foundation; (C) serves as a leader, officer, director, or organizer of a student organization recognized by the institution of higher education at which the student is enrolled at time of an incident or conduct that leads to the suspension or expulsion of such organization from such institution; (D) is suspended or expelled by the institution of higher education at which the student is enrolled due to a violation of the institution\u2019s code of conduct or other disciplinary action by the institution; or (E) is convicted by any Federal, State, or local court of competent jurisdiction of a felony. (2) (A) The Foundation may not stop the payments provided in this Act without first affording the student\u2014 (i) reasonable notice, which shall include the reason for stopping such payments identified under subsection (a) or subsection (c)(1) and any additional relevant information, as determined by the Foundation; and (ii) opportunity for a hearing. (B) If the Foundation, after reasonable notice and opportunity for hearing, finds that a student does not meet the conditions of receiving payment in accordance with subsection (a) or subsection (c)(1), the Foundation shall\u2014 (i) stop the payments provided in this Act for such student; and (ii) provide written notice to such student, which shall include the reason for stopping such payments identified under subsection (a) or subsection (c)(1) and any additional relevant information, as determined by the Foundation. (d) A student whose payments are stopped pursuant to subsection (a) or subsection (c)(1) or an individual who fails to be employed in public service for three out of the first seven years of employment following completion of the graduate degree for which the individual used such payments shall repay to the Foundation an amount equal to the sum of\u2014 (1) the total amount of payments provided in this Act to such student; and (2) interest at the rate of 6 percent per annum on the total amount described in paragraph (1). (e) The Foundation shall ensure all scholarship recipients are notified of the conditions that apply to receiving payments provided in this Act as described in this section, prior to the date of the first such payment. .\n#### 6. Executive Secretary of Foundation\n##### (a) In general\nSection 12 of the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2011 ) is amended\u2014\n**(1)**\nin subsection (a), by striking who shall be appointed by the Board and inserting who shall be appointed by an affirmative vote of not less than two-thirds of the members of the Board ; and\n**(2)**\nby adding at the end the following:\n(c) The Executive Secretary shall serve a term of 4 years and may be reappointed to up to two additional terms of four years in accordance with subsection (a). .\n##### (b) Appointment\nNot later than 90 days after a quorum of the members of the Board of Trustees of the Harry S Truman Scholarship Foundation have been appointed in accordance with section 3(b)(2) of this Act, the Board shall appoint an Executive Secretary of the Foundation in accordance with section 12 of the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2011 ), as amended by subsection (a).\n##### (c) Service of incumbent\nThe individual serving as Executive Secretary of the Harry S Truman Scholarship Foundation as of the date of enactment of this Act may only continue serving in such position until the earlier of\u2014\n**(1)**\nthe date on which the Board of Trustees of the Foundation appoints a new Executive Secretary in accordance with subsection (b); or\n**(2)**\nthe expiration of the 90 day period beginning on the date that a quorum of the members of the Board have been appointed in accordance with section 3(b)(2).\n#### 7. Transparency provisions\nSection 13 of the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2012 ) is amended by adding at the end the following:\n(c) (1) The Foundation shall preserve in unaltered format, and make available on a publicly accessible website of the Foundation, the following materials of the Foundation: (A) Press releases. (B) Program announcements. (C) Biographies of scholarship recipients. (2) The materials described in paragraph (1) may not be deleted, hidden, or password-protected. (3) Any edits made to the materials described in paragraph (1) after such materials were initially published shall be clearly identified and, in a case in which an edit has been made to such materials, a copy of the original, unaltered materials shall remain available to the public on a website of the Foundation. (4) The requirements of this subsection shall apply to any materials published by the Foundation before, on, or after the date of enactment of this subsection. .\n#### 8. Effective date and applicability\n##### (a) Applicability\nThis Act and the amendments made by this Act shall apply only with respect to scholarships awarded under the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2002 ) on or after the date of enactment of this Act.\n##### (b) Treatment of previously awarded scholarships\nNothing in this Act or the amendments made by this Act shall be construed to invalidate or revoke, or alter the terms and conditions of, a scholarship that was awarded under the Harry S Truman Memorial Scholarship Act ( 20 U.S.C. 2002 ) before the date of enactment of this Act. The Harry S Truman foundation shall take such steps as may be necessary to continue to fund and administer such previously awarded scholarships.",
      "versionDate": "2026-03-12",
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
            "name": "Academic performance and assessments",
            "updateDate": "2026-04-02T18:44:06Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2026-04-02T18:43:42Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-02T18:43:49Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-02T18:44:17Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-04-02T18:43:54Z"
          },
          {
            "name": "School administration",
            "updateDate": "2026-04-02T18:44:11Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-04-02T18:43:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-03-16T15:55:02Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7894ih.xml"
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
      "title": "Truman Scholarship Clean House Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Truman Scholarship Clean House Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-13T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make improvements to the Harry S Truman Memorial Scholarship Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T08:19:22Z"
    }
  ]
}
```
