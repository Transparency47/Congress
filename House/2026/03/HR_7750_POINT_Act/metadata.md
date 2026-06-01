# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7750?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7750
- Title: POINT Act
- Congress: 119
- Bill type: HR
- Bill number: 7750
- Origin chamber: House
- Introduced date: 2026-03-02
- Update date: 2026-03-19T19:45:25Z
- Update date including text: 2026-03-19T19:45:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-02: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-02 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Sponsor introductory remarks on measure. (CR H2453)
- Latest action: 2026-03-02: Introduced in House

## Actions

- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-02 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Sponsor introductory remarks on measure. (CR H2453)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7750",
    "number": "7750",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000606",
        "district": "16",
        "firstName": "George",
        "fullName": "Rep. Latimer, George [D-NY-16]",
        "lastName": "Latimer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "POINT Act",
    "type": "HR",
    "updateDate": "2026-03-19T19:45:25Z",
    "updateDateIncludingText": "2026-03-19T19:45:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2453)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-02",
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
          "date": "2026-03-02T14:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-02T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7750ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7750\nIN THE HOUSE OF REPRESENTATIVES\nMarch 2, 2026 Mr. Latimer introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prevent election interference.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Integrity and Nation from Tyranny Act or the POINT Act .\n#### 2. Prevention of executive power to influence an authorized State election\n##### (a) Prohibition\nChapter 13 of title 18, United States Code, is amended by inserting after section 245 the following:\n245a. Prohibition on executive election interference (a) In general Whoever, being a covered individual, knowingly engages in election interference, or uses, provides, or loans any government property, personnel, or resources for the purpose of engaging in election interference, shall be fined under this title, imprisoned not more than 5 years, or both. (b) Definitions In this section: (1) The term election interference \u2014 (A) means conduct by a covered individual that\u2014 (i) violates Federal criminal, voting rights, or campaign finance law; or (ii) includes any fraudulent, deceptive, or unlawful act or attempted act, or knowing use of information acquired by theft, undertaken with the specific intent to significantly influence voters, undermine public confidence in election processes or institutions, or influence, undermine confidence in, or alter the result or reported result of, a general or primary Federal, State, or local election or caucus, including\u2014 (I) the campaign of a candidate; or (II) a ballot measure, including an amendment, a bond issue, an initiative, a recall, a referral, or a referendum; and (B) includes\u2014 (i) causing or inciting the obstruction of the certification of electoral votes by Congress; (ii) communicating to a Federal, State, or local official with the purpose of influencing or altering vote results or the delegation or nomination of electors; (iii) communicating to a Federal, State, or local official with the purpose of publishing or disseminating unsubstantiated claims of fraud, criminal activity, errors, or mismanagement associated with the conducting of a Federal, State, or local election; (iv) communicating to a Federal, State, or local official with the purpose of causing the postponement, prevention, or delay of a Federal, State, or local election; or (v) except to the extent permitted by the Voting Rights Act of 1965, soliciting or ordering the use of personnel, appropriations, or other resources of the Department of Justice to cause the postponement, prevention, or delay of an election, or in order to influence or alter vote results or the delegation or nomination of electors. (2) The term covered individual means\u2014 (A) the President; (B) the Vice President; (C) an employee of the Executive Office of the President; (D) the Attorney General; (E) the Director of the Federal Bureau of Investigation; (F) the Director of National Intelligence; or (G) a cabinet secretary, agency director or any subordinate thereof in a managerial position in such department or agency. (3) The term government property or resources means\u2014 (A) any building, land, vehicle (including aircraft), or other real property owned, leased, or occupied by any department, agency, or instrumentality of the United States (including the White House (except for the Executive Residence), the Department of Defense, the United States Postal Service, or the National Park Service), or any other instrumentality wholly owned by the United States; (B) an information system used or operated by any department, agency, or instrumentality of the United States, by a contractor of any department, agency, or instrumentality of the United States, or by another organization on behalf of any department, agency, or instrumentality of the United States; or (C) funding appropriated by Congress. .\n##### (b) Clerical amendment\nThe table of sections for chapter 13 of title 18, United States Code, is amended by inserting after section 245 the following:\n245a. Prohibition on executive election interference. .\n#### 3. Limitation on use of Armed Forces in the United States\n##### (a) Limitation\nThe President may not deploy members of the Armed Forces or exercise Federal law enforcement authority of the United States in a State where such deployment or exercise of authority would likely disrupt, postpone, delay, prevent, or influence the result of an election (including a referendum or a ballot question), except as follows:\n**(1)**\nFor the purpose of enforcing the Voting Rights Act of 1965.\n**(2)**\nIn the case of an election held or conducted by a State that directly relates to secession from, or armed rebellion against, the United States.\n##### (b) Judicial review\n**(1) Right of review**\nAny State in which the President deploys members of the Armed Forces or exercises the Federal law enforcement authority of the United States in violation of subsection (a) may bring an action against the United States in the appropriate district court of the United States for appropriate relief, including injunctive relief.\n**(2) Burden of proof**\nNotwithstanding any other provision of law, in an action under this section, the President shall have the burden of proving that such violation did not occur.\n**(3) Expedited appeals**\n**(A) Time for appeal to court of appeals**\nNotwithstanding section 2107 of title 28, United States Code, a notice of appeal of a final judgment issued in an action brought under paragraph (1) may be filed not later than 15 days after such judgement is entered.\n**(B) Time for petition to Supreme Court**\nNotwithstanding section 2101 of title 28, United States Code, a petition for a writ of certiorari may be filed not later than 15 days after the court of appeals enters a final judgement.\n**(4) Expedited consideration**\nIt shall be the duty of the applicable district court of the United States, the applicable court of appeals of the United States, and the Supreme Court of the United States to advance on the docket and to expedite to the greatest possible extent the disposition of any matter brought under this section.\n#### 4. Prevention of President or Congress from preempting a State\u2019s constitutional rights\n##### (a) Cause of action\nA State harmed by a violation of any of the rights described in subsection (b) may bring an action against the United States in the appropriate district court of the United States for appropriate relief, including injunctive relief.\n##### (b) Rights\nThe rights described in this section are the following:\n**(1)**\nThe Full Faith and Credit Clause (Const. Art. IV Sec. 1).\n**(2)**\nThe right of a State legislature to consent to the formation of a new State within its jurisdiction, or the formation of a State within its jurisdiction with two or more States or parts of its State (Const. Art. IV Sec. 3).\n**(3)**\nThe guarantee by the United States to every State of a republican form of government, protection against military invasion, and upon application of the legislature, or of the executive (when the legislature cannot be convened) against domestic violence (Const. Art. IV Sec. 4).\n**(4)**\nThe rights of three fourths of the several States to ratify an amendment to the Constitution and the right of a State to not be deprived of its equal suffrage in the Senate (Const. Art. V).\n**(5)**\nThe reservation to the States respectively, or the people, any powers not delegated to the United States by the Constitution nor prohibited by it to the States (Const. Amendment X).\n**(6)**\nThe right of lawfully chosen electors for President and Vice President to meet in their respective States in order to vote by ballot, and to prepare a signed and certified list of ballots cast for transmission under seal to the seat of government, directed to the President of the Senate (Const. Amendment X).\n##### (c) Expedited appeals\n**(1) Time for appeal to court of appeals**\nNotwithstanding section 2107 of title 28, United States Code, a notice of appeal of a final judgment issued in an action brought under subsection (a) may be filed not later than 15 days after such judgement is entered.\n**(2) Time for petition to Supreme Court**\nNotwithstanding section 2101 of title 28, United States Code, a petition for a writ of certiorari may be filed not later than 15 days after the court of appeals enters a final judgement.\n##### (d) Expedited consideration\nIt shall be the duty of the applicable district court of the United States, the applicable court of appeals of the United States, and the Supreme Court of the United States to advance on the docket and to expedite to the greatest possible extent the disposition of any matter brought under this section.",
      "versionDate": "2026-03-02",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-19T19:45:25Z"
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
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7750ih.xml"
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
      "title": "POINT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POINT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Integrity and Nation from Tyranny Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent election interference.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T04:48:30Z"
    }
  ]
}
```
