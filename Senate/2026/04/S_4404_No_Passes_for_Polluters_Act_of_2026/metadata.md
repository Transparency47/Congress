# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4404?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4404
- Title: No Passes for Polluters Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4404
- Origin chamber: Senate
- Introduced date: 2026-04-27
- Update date: 2026-05-18T18:20:00Z
- Update date including text: 2026-05-18T18:20:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in Senate
- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-04-27: Introduced in Senate

## Actions

- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4404",
    "number": "4404",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "No Passes for Polluters Act of 2026",
    "type": "S",
    "updateDate": "2026-05-18T18:20:00Z",
    "updateDateIncludingText": "2026-05-18T18:20:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T23:00:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4404is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4404\nIN THE SENATE OF THE UNITED STATES\nApril 27, 2026 Mr. Whitehouse (for himself and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Clean Air Act to require Congress to approve of the application of certain executive exemptions under that Act, to strike an exemption under that Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Passes for Polluters Act of 2026 .\n#### 2. Congressional approval of use of exemptions under the Clean Air Act\n##### (a) Approval process\n**(1) In general**\nTitle III of the Clean Air Act ( 42 U.S.C. 7601 et seq. ) is amended by adding at the end the following:\n330. Congressional approval of use of exemptions (a) Definitions In this section: (1) Comptroller General The term Comptroller General means the Comptroller General of the United States. (2) Covered exemption (A) In general The term covered exemption means an exemption, including the adoption of regulations or issuance of orders, as applicable, under\u2014 (i) section 118(b); (ii) section 248(e); and (iii) section 604(f). (B) Inclusion The term covered exemption includes an extension of a covered exemption, if that extension is authorized under applicable law. (3) Joint resolution The term joint resolution means a joint resolution of the House of Representatives or the Senate that only expresses the approval of Congress of a proposed use of a covered exemption set forth in a special message. (4) Special message The term special message means a special message transmitted by the President to the Senate and the House of Representatives pursuant to subsection (c)(1). (b) Limitation on use of exemptions Notwithstanding any other provision of this Act\u2014 (1) neither the President, the Administrator, the head of any Federal department or agency, nor any office or employee of the United States may use a covered exemption or, as applicable, extend a covered exemption except after a joint resolution is enacted in accordance with this section; and (2) neither the use of a covered exemption nor, as applicable, the extension of a covered exemption shall have any force or effect except after a joint resolution is enacted in accordance with this section. (c) Proposed use of exemption (1) Transmittal of special message Whenever the President, the Administrator, the head of any Federal department or agency, or any officer or employee of the United States proposes to use a covered exemption, the President shall transmit to the Senate and the House of Representatives, electronically or through physical means, a special message describing\u2014 (A) the covered exemption proposed to be used; (B) the period of time during which the covered exemption is proposed to be used; (C) the reasons for the proposed use of a covered exemption, including any legal authority invoked to justify that proposed use; and (D) all facts, circumstances, and considerations relating to or bearing on the proposed use of the covered exemption, including\u2014 (i) an analysis of the application of those facts, circumstances and considerations to any legal authority invoked to justify the proposed use of the covered exemption; and (ii) to the maximum extent practicable, the estimated effect of the proposed use. (2) Inclusion of multiple uses A special message may include 1 or more proposed uses of covered exemptions. (3) Consistency with legislative policy (A) In general The use of a covered exemption shall only be permissible as specifically provided by law. (B) Limitation No officer or employee of the United States may use a covered exemption for any purpose other than a purpose described in subparagraph (A). (d) Transmission of special messages; publication (1) Delivery to Houses of Congress (A) In general Each special message shall\u2014 (i) be transmitted to the Senate and the House of Representatives on the same day; (ii) if the Senate is not in session on the day the special message is transmitted, be delivered to the Secretary of the Senate; and (iii) if the House of Representatives is not in session on the day the special message is transmitted, be delivered to the Clerk of the House of Representatives. (B) Committee referral; printing Each special message transmitted to the Senate and the House of Representatives shall\u2014 (i) be referred to the appropriate committee of the Senate and the House of Representatives; and (ii) be printed as a document of each House. (2) Delivery to Comptroller General (A) In general A copy of each special message shall be transmitted to the Comptroller General on the same day that the special message is transmitted to the Senate and the House of Representatives. (B) Notification In order to assist Congress in the exercise of the functions of Congress under this section, the Comptroller General shall review each special message and notify the Senate and the House of Representatives as soon as practicable as to\u2014 (i) the facts surrounding the proposed use of the applicable covered exemption; and (ii) whether or not (or to what extent), in the judgment of the Comptroller General, the proposed use of the applicable covered exemption is in accordance with existing statutory authority. (3) Transmission of supplementary messages (A) In general If any information contained in a special message is subsequently revised, the President shall transmit to both Houses of Congress and the Comptroller General a supplementary message stating and explaining the revision. (B) Applicability of provisions Any supplementary message under subparagraph (A) shall be delivered, referred, and printed as provided in paragraph (1). (C) Comptroller General notification The Comptroller General shall promptly notify the Senate and the House of Representatives of any change in the notification under paragraph (2)(B) that may necessitated by the supplementary message under subparagraph (A). (4) Printing in Federal Register Any special message transmitted to Congress, and any supplementary message transmitted to Congress under paragraph (3)(A), shall be printed in the first issue of the Federal Register published after the transmission. (5) Cumulative reports (A) In general Not later than the 10th day of each month during a fiscal year, the President shall submit to the Senate and the House of Representatives a report that describes\u2014 (i) as of the first day of that month, each special message transmitted to Congress during the previous month; and (ii) with respect to each special message transmitted to Congress during the previous month, the information required to be submitted in that special message. (B) Publication Each report submitted under subparagraph (A) shall be printed in the first issue of the Federal Register published after the submission of the report to the Senate and the House of Representatives. (e) Reports by Comptroller General (1) In general The Comptroller General shall submit to both Houses of Congress a report described in paragraph (2) if the Comptroller General finds that\u2014 (A) the President, the Administrator, the head of any department or agency of the United States, or any other officer or employee of the United States has ordered, permitted, or approved the use of an exemption under this Act that is a covered exemption; and (B) the President has failed to transmit a special message with respect to the use of the covered exemption. (2) Report A report under paragraph (1) shall include any available information concerning the use of a covered exemption described in that paragraph. (3) Applicability With respect to a report under paragraph (1)\u2014 (A) the provisions of this section shall apply to the proposed use of a covered exemption described in that report in the same manner and with the same effect as if the report were a special message transmitted by the President; and (B) for purposes of this section, the report shall be considered a special message. (f) Procedure in the Senate and House (1) Referral Any joint resolution introduced with respect to a special message shall be referred to the Committee on Environment and Public Works of the Senate or the Committee on Energy and Commerce of the House of Representatives, as applicable. (2) Discharge of committee (A) In general If the committee to which a joint resolution has been referred has not reported the joint resolution by the end of the 15-session day period that begins on the date of the introduction of the joint resolution, it shall be in order to move\u2014 (i) to discharge the committee from further consideration of the joint resolution; or (ii) to discharge the committee from further consideration of any other joint resolution with respect to the same special message with respect to the same proposed use of a covered exemption, as the case may be, that has been referred to the committee. (B) Procedure on floor (i) Motion to discharge A motion to discharge described in subparagraph (A)\u2014 (I) may be made only\u2014 (aa) by an individual favoring the joint resolution; and (bb) if supported by 1/5 of the Members of the applicable House (a quorum being present); and (II) may not be made after the committee has reported a joint resolution with respect to the same special message. (ii) Status A motion to discharge described in subparagraph (A) is\u2014 (I) privileged in the Senate; and (II) highly privileged in the House of Representatives. (iii) Debate Debate on a motion to discharge in described in subparagraph (A) shall be limited to not more than 1 hour in each House, the time for which\u2014 (I) in the Senate, shall be divided equally between, and controlled by, the majority leader and the minority leader (or their designees); and (II) in the House of Representatives, shall be divided equally between those favoring and those opposing the joint resolution. (iv) No amendment No amendment to a motion to discharge described in subparagraph (A) shall be in order. (v) No motion to reconsider It shall not be in order to move to reconsider the vote by which a motion to discharge described in subparagraph (A) is agreed to or disagreed to. (3) Floor consideration in the Senate (A) Debate Debate in the Senate on any joint resolution and debatable motions and appeals in connection with that joint resolution shall be limited to not more than 10 hours, with the time to be equally divided between, and controlled by, the majority leader and the minority leader (or their designees). (B) Motion to further limit debate A motion to further limit debate on a joint resolution is not debatable in the Senate. (C) No amendments or motions to recommit No amendment to or motion to recommit a joint resolution is in order in the Senate. (D) Vote required The Senate may only agree to a joint resolution on the affirmative vote of 2/3 of the Members of the Senate present and voting. (4) Procedure in the House (A) Motion to proceed (i) In general When the Committee on Energy and Commerce of the House of Representatives has reported, or has been discharged from further consideration, a joint resolution, it shall at any time thereafter be in order (even though a previous motion to the same effect has been disagreed to) to move to proceed to the consideration of the joint resolution. (ii) Status A motion under clause (i) shall be highly privileged and not debatable. (iii) No amendments or motions to reconsider No amendment to or motion to reconsider a motion under clause (i) shall be in order. (B) Debate (i) In general Debate on a joint resolution shall be limited to not more than 2 hours, which shall be divided equally between those favoring and those opposing the joint resolution. (ii) Motion to further limit debate A motion to further limit debate on a joint resolution in the House of Representatives shall not be debatable. (iii) No amendments or motions to recommit No amendment to or motion to recommit a joint resolution in the House of Representatives is in order. (iv) No motion to reconsider It shall not be in order to move to reconsider the vote by which a joint resolution is agreed to or disagreed to in the House of Representatives. (v) Appeals All appeals from the decisions of the Chair relating to the application of the Rules of the House of Representatives to the procedure relating to a joint resolution shall be decided without debate. (vi) Applicability of rules Except to the extent specifically provided in this paragraph, consideration of a joint resolution shall be governed by the Rules of the House of Representatives applicable to other joint resolutions in similar circumstances. (C) Vote required The House of Representatives may only agree to a joint resolution on the affirmative vote of 2/3 of the Members of the House of Representatives present and voting. (5) Continuity of Congress For purposes of any time limit under this section\u2014 (A) the continuity of a session of Congress shall be considered broken only by an adjournment of Congress sine die; and (B) the days on which either House is not in session because of an adjournment of more than 3 days to a day certain shall be excluded in the computation of the 15-day period described in paragraph (2)(A). (6) Exercise of rulemaking powers This subsection is enacted\u2014 (A) as an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, but only with respect to the procedure to be followed in the House in the case of joint resolutions, and supersedes other rules only to the extent that it is inconsistent with such other rules; and (B) with full recognition of the constitutional right of either House to change the rules (relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House. (g) Enforcement A person may commence a civil action under section 304 on his or her own behalf against any person (including, notwithstanding any provision of that section, the United States, the President, the Administrator, the head of any Federal department or agency, and any officer or employee of the United States) who is alleged to use a covered exemption a joint resolution for which has not been enacted in accordance with this section. .\n**(2) Conforming amendment**\nSection 304(b) of the Clean Air Act ( 42 U.S.C. 7604(b) ) is amended, in the undesignated matter following paragraph (2), by striking (f)(4) and inserting (f)(4), a civil action described in section 330(g), or .\n##### (b) Other amendments\n**(1) Exemption of executive branch emissions from requirements under the Clean Air Act**\nSection 118(b) of the Clean Air Act ( 42 U.S.C. 7418(b) ) is amended\u2014\n**(A)**\nby striking the sixth sentence;\n**(B)**\nby striking the fifth sentence and inserting the following:\n(B) Reconsideration The President shall reconsider the need for any regulations issued under subparagraph (A) at 3-year intervals. ;\n**(C)**\nin the fourth sentence\u2014\n**(i)**\nby inserting and subject to the enactment of a joint resolution under section 330 authorizing the regulations after to do so ;\n**(ii)**\nby striking he determines and inserting the President determines ; and\n**(iii)**\nby striking In addition to any such exemption of a particular emission source and inserting the following:\n(2) Exemption for military property (A) In general In addition to any exemption of a particular emission source under paragraph (1) ;\n**(D)**\nin the third sentence\u2014\n**(i)**\nby inserting , subject to the enactment of a new joint resolution under section 330 authorizing the extension, after exemptions may ; and\n**(ii)**\nby striking Any exemption and inserting the following:\n(C) Term; extension Any exemption ;\n**(E)**\nin the second sentence, by striking No such extension shall be granted due to and inserting the following:\n(B) Requirement The President may not propose under section 330 to use an exemption under subparagraph (A) as a result of a ; and\n**(F)**\nin the first sentence, by striking (b) The President and all that follows through he determines and inserting the following:\n(b) Exemptions (1) Executive branch (A) In general The President may, subject to the enactment of a joint resolution under section 330 authorizing the exemption, exempt any emission source of any department, agency, or instrumentality in the executive branch from compliance with such a requirement if the President determines .\n**(2) Exemption from Federal agency fleet requirements**\nSection 248(e) of the Clean Air Act ( 42 U.S.C. 7588(e) ) is amended by inserting , subject to the enactment of a joint resolution under section 330 authorizing the exemption before the period at the end.\n**(3) Exemption from phase-out of production and consumption of certain substances**\nSection 604(f) of the Clean Air Act ( 42 U.S.C. 7671c(f) ) is amended\u2014\n**(A)**\nin the eighth sentence, by striking No exemption shall be granted under this paragraph due to and inserting the following:\n(3) Requirement The President may not propose under section 330 to issue an order under this subsection as a result of a ;\n**(B)**\nin the seventh sentence, by striking Each such additional exemption and inserting the following:\n(B) Period Each additional exemption under subparagraph (A) ;\n**(C)**\nby striking the sixth sentence and inserting the following:\n(2) Extensions (A) In general The President may, subject to the enactment of a new joint resolution under section 330 authorizing the additional exemption, grant additional exemptions under this subsection. ;\n**(D)**\nby striking the third, fourth, and fifth sentences and inserting the following:\n(C) Period An exemption under subparagraph (A) shall be for a specified period, which may not exceed 1 year. ;\n**(E)**\nin the second sentence, by striking Such orders and inserting the following:\n(B) Scope An order under subparagraph (A) ; and\n**(F)**\nin the first sentence\u2014\n**(i)**\nby inserting , before seeking that joint resolution, after if the President ;\n**(ii)**\nby inserting and subject to the enactment of a joint resolution under section 330 authorizing the order after Montreal Protocol ; and\n**(iii)**\nby striking The President and inserting the following:\n(1) Orders (A) In general The President .\n#### 3. Repeal of exemption from schedule for compliance for hazardous air pollutants\n##### (a) In general\nSection 112(i) of the Clean Air Act ( 42 U.S.C. 7412(i) ) is amended\u2014\n**(1)**\nin paragraph (3)(A), by striking paragraphs (4) through (8) and inserting paragraphs (4) through (7) ;\n**(2)**\nby striking paragraph (4); and\n**(3)**\nby redesignating paragraphs (5) through (8) as paragraphs (4) through (7), respectively.\n##### (b) Conforming amendments\n**(1)**\nSection 112 of the Clean Air Act ( 42 U.S.C. 7412 ) is amended\u2014\n**(A)**\nin subsection (d)(8)(C), in the first sentence, by striking subsection (i)(8) and inserting subsection (i)(7) ; and\n**(B)**\nin subsection (j)(5)\u2014\n**(i)**\nin the second sentence, by striking subsection (i)(5) and inserting subsection (i)(4) ; and\n**(ii)**\nin the third sentence, by striking subsection (i)(5)(A) and inserting subsection (i)(4)(A) .\n**(2)**\nParagraph (1)(A) of section 118(b) of the Clean Air Act ( 42 U.S.C. 7418(b) ) (as amended by section 2(b)(1)) is amended, in the first sentence, by striking , and an exemption from section 112 may be granted only in accordance with section 112(i)(4) .",
      "versionDate": "2026-04-27",
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
        "name": "Environmental Protection",
        "updateDate": "2026-05-18T18:19:59Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4404is.xml"
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
      "title": "No Passes for Polluters Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Passes for Polluters Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Clean Air Act to require Congress to approve of the application of certain executive exemptions under that Act, to strike an exemption under that Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:34Z"
    }
  ]
}
```
