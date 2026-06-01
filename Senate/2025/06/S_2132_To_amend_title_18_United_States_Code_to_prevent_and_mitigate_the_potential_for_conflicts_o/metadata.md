# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2132
- Title: CLEAR Path Act
- Congress: 119
- Bill type: S
- Bill number: 2132
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-05-02T01:54:55Z
- Update date including text: 2026-05-02T01:54:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-01-15 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-01-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-01-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-01-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 305.
- 2026-04-21 - Floor: Passed Senate with an amendment by Voice Vote. (consideration: CR S1854; text of amendment in the nature of a substitute: CR S1854-1855)
- 2026-04-21 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Voice Vote.
- 2026-04-22 - Floor: Message on Senate action sent to the House.
- 2026-04-22 13:35:36 - Floor: Received in the House.
- 2026-04-22 13:41:23 - Floor: Held at the desk.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-01-15 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-01-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-01-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-01-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 305.
- 2026-04-21 - Floor: Passed Senate with an amendment by Voice Vote. (consideration: CR S1854; text of amendment in the nature of a substitute: CR S1854-1855)
- 2026-04-21 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Voice Vote.
- 2026-04-22 - Floor: Message on Senate action sent to the House.
- 2026-04-22 13:35:36 - Floor: Received in the House.
- 2026-04-22 13:41:23 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2132",
    "number": "2132",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "CLEAR Path Act",
    "type": "S",
    "updateDate": "2026-05-02T01:54:55Z",
    "updateDateIncludingText": "2026-05-02T01:54:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-04-22",
      "actionTime": "13:41:23",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-04-22",
      "actionTime": "13:35:36",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Voice Vote. (consideration: CR S1854; text of amendment in the nature of a substitute: CR S1854-1855)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Voice Vote.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-01-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 305.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-01-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-01-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
            "date": "2026-01-28T16:59:15Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-15T14:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-18T19:02:00Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-18T19:02:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "VT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "ID"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "RI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2132is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2132\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Cornyn (for himself, Mr. Welch , Mr. Risch , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prevent and mitigate the potential for conflicts of interest following government service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Conflict-free Leaving Employment and Activity Restrictions Path Act or the CLEAR Path Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nCongress and the executive branch have recognized the importance of preventing and mitigating the potential for conflicts of interest following government service, including with respect to senior United States officials working on behalf of foreign governments; and\n**(2)**\nCongress and the executive branch should jointly evaluate the status and scope of post-employment restrictions.\n#### 3. Post-employment restrictions on officials in positions subject to Senate confirmation\n##### (a) In general\nSection 207 of title 18, United States Code, is amended by adding at the end the following:\n(m) Extended post-Employment restrictions for officials in positions subject to Senate confirmation (1) Definitions In this subsection: (A) Country of concern The term country of concern has the meaning given the term in section 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ). (B) Foreign governmental entity The term foreign governmental entity has the meaning given the term in section 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ). (C) Represent The term represent does not include representation by an attorney, who is duly licensed and authorized to provide legal advice in a United States jurisdiction, of a person or entity in a legal capacity or for the purposes of rendering legal advice. (D) Senate-confirmed position The term Senate-confirmed position means a position in a department or agency of the executive branch of the United States for which appointment is required to be made by the President, by and with the advice and consent of the Senate. (2) Agency heads, deputy heads, and other positions subject to Senate confirmation With respect to a person serving as the head or deputy head of, or serving in any Senate-confirmed position in, a department or agency of the executive branch of the United States, the restrictions described in subsection (f)(1) shall apply to any such person who knowingly represents, aids, or advises a foreign governmental entity of a country of concern before an officer or employee of the executive or legislative branch of the United States with the intent to influence a decision of the officer or employee in carrying out his or her official duties at any time after the termination of the person\u2019s service in that position. (3) Notice of restrictions Any person subject to the restrictions under this subsection shall be provided notice of these restrictions by the relevant department or agency\u2014 (A) upon appointment by the President; and (B) upon termination of service with the relevant department or agency. (4) Effective date The restrictions under this subsection shall apply only to persons who are appointed by the President to the positions referenced in this section on or after the date of enactment of the Conflict-free Leaving Employment and Activity Restrictions Path Act . (5) Sunset The restrictions under this subsection shall expire on the date that is 5 years after the date of enactment of the Conflict-free Leaving Employment and Activity Restrictions Path Act . .\n##### (b) Conforming amendment\nSection 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (6) and (7) as paragraphs (8) and (9), respectively; and\n**(2)**\nby inserting after paragraph (5) the following:\n(6) Relation to government-wide restrictions This subsection shall not apply to a person by reason of the person\u2019s service in a position referenced in this subsection if the person is subject to the restrictions under section 207(m) of title 18, United States Code, by reason of the same service. .\n#### 4. Mechanism to amend definition of country of concern\nSection 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ) is amended by inserting after paragraph (6), as added by section 3(b), the end the following:\n(7) Modification to definition of country of concern (A) In general The Secretary of State may, in consultation with the Attorney General, propose the addition or deletion of countries described in paragraph (1)(A). (B) Submission Any proposal described in subparagraph (A) shall\u2014 (i) be submitted to the Chairman and Ranking Member of the Committee on Foreign Relations of the Senate and the Chairman and Ranking Member of the Committee on the Judiciary of the House of Representatives; and (ii) become effective upon enactment of a joint resolution of approval as described in subparagraph (C). (C) Joint resolution of approval (i) In general For purposes of subparagraph (B)(ii), the term joint resolution of approval means only a joint resolution\u2014 (I) that does not have a preamble; (II) that includes in the matter after the resolving clause the following: That Congress approves the modification of the definition of country of concern under section 1(m) of the State Department Basic Authorities Act of 1956, as submitted by the Secretary of State on ____; and section 1(m)(1)(A) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m)(1)(A) ) is amended by ______. , the blank spaces being appropriately filled in with the appropriate date and the amendatory language required to modify the list of countries in paragraph (1)(A) of this subsection by adding or deleting 1 or more countries; and (III) the title of which is as follows: Joint resolution approving modifications to definition of country of concern under section 1(m) of the State Department Basic Authorities Act of 1956. . (ii) Referral (I) Senate A resolution described in clause (i) that is introduced in the Senate shall be referred to the Committee on Foreign Relations of the Senate. (II) House of Representatives A resolution described in clause (i) that is introduced in the House of Representatives shall be referred to the Committee on the Judiciary of the House of Representatives. .",
      "versionDate": "2025-06-18",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2132rs.xml",
      "text": "II\nCalendar No. 305\n119th CONGRESS\n2d Session\nS. 2132\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Cornyn (for himself, Mr. Welch , Mr. Risch , Mr. Whitehouse , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nJanuary 28, 2026 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend title 18, United States Code, to prevent and mitigate the potential for conflicts of interest following government service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Conflict-free Leaving Employment and Activity Restrictions Path Act or the CLEAR Path Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nCongress and the executive branch have recognized the importance of preventing and mitigating the potential for conflicts of interest following government service, including with respect to senior United States officials working on behalf of foreign governments; and\n**(2)**\nCongress and the executive branch should jointly evaluate the status and scope of post-employment restrictions.\n#### 3. Post-employment restrictions on officials in positions subject to Senate confirmation\n##### (a) In general\nSection 207 of title 18, United States Code, is amended by adding at the end the following:\n(m) Extended post-Employment restrictions for officials in positions subject to Senate confirmation (1) Definitions In this subsection: (A) Country of concern The term country of concern has the meaning given the term in section 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ). (B) Foreign governmental entity The term foreign governmental entity has the meaning given the term in section 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ). (C) Represent The term represent does not include representation by an attorney, who is duly licensed and authorized to provide legal advice in a United States jurisdiction, of a person or entity in a legal capacity or for the purposes of rendering legal advice. (D) Senate-confirmed position The term Senate-confirmed position means a position in a department or agency of the executive branch of the United States for which appointment is required to be made by the President, by and with the advice and consent of the Senate. (2) Agency heads, deputy heads, and other positions subject to Senate confirmation With respect to a person serving as the head or deputy head of, or serving in any Senate-confirmed position in, a department or agency of the executive branch of the United States, the restrictions described in subsection (f)(1) shall apply to any such person who knowingly represents, aids, or advises a foreign governmental entity of a country of concern before an officer or employee of the executive or legislative branch of the United States with the intent to influence a decision of the officer or employee in carrying out his or her official duties at any time after the termination of the person\u2019s service in that position. (3) Notice of restrictions Any person subject to the restrictions under this subsection shall be provided notice of these restrictions by the relevant department or agency\u2014 (A) upon appointment by the President; and (B) upon termination of service with the relevant department or agency. (4) Effective date The restrictions under this subsection shall apply only to persons who are appointed by the President to the positions referenced in this section on or after the date of enactment of the Conflict-free Leaving Employment and Activity Restrictions Path Act . (5) Sunset The restrictions under this subsection shall expire on the date that is 5 years after the date of enactment of the Conflict-free Leaving Employment and Activity Restrictions Path Act . .\n##### (b) Conforming amendment\nSection 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (6) and (7) as paragraphs (8) and (9), respectively; and\n**(2)**\nby inserting after paragraph (5) the following:\n(6) Relation to government-wide restrictions This subsection shall not apply to a person by reason of the person\u2019s service in a position referenced in this subsection if the person is subject to the restrictions under section 207(m) of title 18, United States Code, by reason of the same service. .\n#### 4. Mechanism to amend definition of country of concern\nSection 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ) is amended by inserting after paragraph (6), as added by section 3(b), the end the following:\n(7) Modification to definition of country of concern (A) In general The Secretary of State may, in consultation with the Attorney General, propose the addition or deletion of countries described in paragraph (1)(A). (B) Submission Any proposal described in subparagraph (A) shall\u2014 (i) be submitted to the Chairman and Ranking Member of the Committee on Foreign Relations of the Senate and the Chairman and Ranking Member of the Committee on the Judiciary of the House of Representatives; and (ii) become effective upon enactment of a joint resolution of approval as described in subparagraph (C). (C) Joint resolution of approval (i) In general For purposes of subparagraph (B)(ii), the term joint resolution of approval means only a joint resolution\u2014 (I) that does not have a preamble; (II) that includes in the matter after the resolving clause the following: That Congress approves the modification of the definition of country of concern under section 1(m) of the State Department Basic Authorities Act of 1956, as submitted by the Secretary of State on ____; and section 1(m)(1)(A) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m)(1)(A) ) is amended by ______. , the blank spaces being appropriately filled in with the appropriate date and the amendatory language required to modify the list of countries in paragraph (1)(A) of this subsection by adding or deleting 1 or more countries; and (III) the title of which is as follows: Joint resolution approving modifications to definition of country of concern under section 1(m) of the State Department Basic Authorities Act of 1956. . (ii) Referral (I) Senate A resolution described in clause (i) that is introduced in the Senate shall be referred to the Committee on Foreign Relations of the Senate. (II) House of Representatives A resolution described in clause (i) that is introduced in the House of Representatives shall be referred to the Committee on the Judiciary of the House of Representatives. .",
      "versionDate": "2026-01-28",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2132es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 2132\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend title 18, United States Code, to prevent and mitigate the potential for conflicts of interest following government service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Conflict-free Leaving Employment and Activity Restrictions Path Act or the CLEAR Path Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nCongress and the executive branch have recognized the importance of preventing and mitigating the potential for conflicts of interest following Government service, including with respect to senior United States officials working on behalf of foreign governments; and\n**(2)**\nCongress and the executive branch should jointly evaluate the status and scope of post-employment restrictions.\n#### 3. Post-employment restrictions on officials in positions subject to Senate confirmation\n##### (a) In general\nSection 207 of title 18, United States Code, is amended by adding at the end the following:\n(m) Extended post-employment restrictions for officials in positions subject to Senate confirmation (1) Definitions In this subsection: (A) Country of concern The term country of concern has the meaning given the term in section 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ), except that it does not include the country described in paragraph (1)(A)(vi) of that section, as in effect on the date of enactment of the Conflict-free Leaving Employment and Activity Restrictions Path Act . (B) Foreign governmental entity The term foreign governmental entity has the meaning given the term in section 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ). (C) Represent The term represent does not include representation by an attorney, who is duly licensed and authorized to provide legal advice in a United States jurisdiction, of a person or entity in a legal capacity or for the purposes of rendering legal advice. (D) Senate-confirmed position The term Senate-confirmed position means a position in a department or agency of the executive branch of the United States for which appointment is required to be made by the President, by and with the advice and consent of the Senate. (2) Agency heads, deputy heads, and other positions subject to Senate confirmation Any person who serves in a position requiring appointment by the President as head or deputy head of, or serves in any other Senate-confirmed position in, a department or agency of the executive branch of the United States, and who, at any time after the termination of the person\u2019s service in that position, knowingly represents, aids, or advises a foreign governmental entity of a country of concern before an officer or employee of the executive or legislative branch of the United States with the intent to influence a decision of the officer or employee in carrying out his or her official duties shall be punished as provided in section 216. (3) Notice of restrictions Any person subject to the restrictions under this subsection shall be provided notice of these restrictions by the relevant department or agency\u2014 (A) upon appointment by the President; and (B) upon termination of service with the relevant department or agency. (4) Effective date (A) In general Except as provided in subparagraph (B), the restrictions under this subsection shall apply only to persons who are appointed by the President to the positions referenced in this subsection on or after the date of enactment of the Conflict-free Leaving Employment and Activity Restrictions Path Act . (B) Grace period for added countries of concern If the definition of the term country of concern under subsection (m) of section 1 of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a ) is modified in accordance with paragraph (7) of that subsection by adding a country to the list of countries described in paragraph (1)(A) of that subsection, in the case of any person who is appointed by the President to a position referenced in this subsection on or after the date of enactment of the Conflict-free Leaving Employment and Activity Restrictions Path Act and who knowingly represents, aids, or advises a foreign governmental entity of a country added to the list of countries described in paragraph (1)(A) of such subsection (m), the restrictions under this subsection shall apply to such person on and after the date that is 30 days after the date of enactment of a relevant joint resolution of approval as described in paragraph (7)(C) of such subsection (m) adding that country to the list of countries described in paragraph (1)(A) of such subsection (m). (5) Sunset (A) In general On and after the date that is 5 years after the date of enactment of the Conflict-free Leaving Employment and Activity Restrictions Path Act , the restrictions under paragraph (2) shall not apply to any person appointed by the President, on or after such date of enactment, to a position referenced in this subsection, without regard to the date on which the service of such person in such position terminates. (B) No effect on conduct before sunset Nothing in subparagraph (A) shall be construed to limit the applicability of paragraph (2) with respect to any conduct by a person appointed by the President to a position referenced in this subsection that occurred before the date that is 5 years after the date of enactment of the Conflict-free Leaving Employment and Activity Restrictions Path Act . .\n##### (b) Conforming amendment\nSection 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (6) and (7) as paragraphs (8) and (9), respectively; and\n**(2)**\nby inserting after paragraph (5) the following:\n(6) Relation to government-wide restrictions This subsection shall not apply to a person by reason of the person\u2019s service in a position referenced in this subsection if the person is subject to the restrictions under section 207(m) of title 18, United States Code, by reason of the same service. .\n#### 4. Mechanism to amend definition of country of concern\nSection 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ) is amended by inserting after paragraph (6), as added by section 3(b), the following:\n(7) Modification to definition of country of concern (A) In general The Secretary of State may, in consultation with the Attorney General, propose the addition or deletion of countries described in paragraph (1)(A). (B) Submission Any proposal described in subparagraph (A) shall\u2014 (i) be submitted to the Chairman and Ranking Member of the Committee on Foreign Relations of the Senate and the Chairman and Ranking Member of the Committee on the Judiciary of the House of Representatives; and (ii) become effective upon enactment of a joint resolution of approval as described in subparagraph (C). (C) Joint resolution of approval (i) In general For purposes of subparagraph (B)(ii), the term joint resolution of approval means only a joint resolution\u2014 (I) that does not have a preamble; (II) that includes in the matter after the resolving clause the following: That Congress approves the modification of the definition of country of concern under section 1(m) of the State Department Basic Authorities Act of 1956, as submitted by the Secretary of State on ____; and section 1(m)(1)(A) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m)(1)(A) ) is amended by ______. , the blank spaces being appropriately filled in with the appropriate date and the amendatory language required to modify the list of countries in paragraph (1)(A) of this subsection by adding or deleting 1 or more countries; and (III) the title of which is as follows: Joint resolution approving modifications to definition of country of concern under section 1(m) of the State Department Basic Authorities Act of 1956. . (ii) Referral (I) Senate A resolution described in clause (i) that is introduced in the Senate shall be referred to the Committee on Foreign Relations of the Senate. (II) House of Representatives A resolution described in clause (i) that is introduced in the House of Representatives shall be referred to the Committee on the Judiciary of the House of Representatives. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-11-18",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on the Judiciary, and Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6106",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CLEAR Path Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Asia",
            "updateDate": "2026-03-10T18:43:08Z"
          },
          {
            "name": "China",
            "updateDate": "2026-03-10T18:43:22Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-10T18:42:57Z"
          },
          {
            "name": "Cuba",
            "updateDate": "2026-03-10T18:43:47Z"
          },
          {
            "name": "Europe",
            "updateDate": "2026-03-10T18:43:16Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2026-03-10T18:42:42Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-03-10T18:42:47Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2026-03-10T18:43:04Z"
          },
          {
            "name": "Iran",
            "updateDate": "2026-03-10T18:43:30Z"
          },
          {
            "name": "Latin America",
            "updateDate": "2026-03-10T18:43:51Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2026-03-10T18:42:52Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2026-03-10T18:43:12Z"
          },
          {
            "name": "North Korea",
            "updateDate": "2026-03-10T18:43:36Z"
          },
          {
            "name": "Russia",
            "updateDate": "2026-03-10T18:43:26Z"
          },
          {
            "name": "Syria",
            "updateDate": "2026-03-10T18:43:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-24T15:48:51Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2132is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2132rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2132es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "CLEAR Path Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "CLEAR Path Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-04-22T03:38:22Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Conflict-free Leaving Employment and Activity Restrictions Path Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-04-22T03:38:22Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Conflict-free Leaving Employment and Activity Restrictions Path Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-01-30T04:08:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "CLEAR Path Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-01-30T04:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CLEAR Path Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Conflict-free Leaving Employment and Activity Restrictions Path Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to prevent and mitigate the potential for conflicts of interest following government service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:34:13Z"
    }
  ]
}
```
