# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1887?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1887
- Title: Vote at Home Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1887
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-01-23T00:08:46Z
- Update date including text: 2026-01-23T00:08:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1887",
    "number": "1887",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Vote at Home Act of 2025",
    "type": "S",
    "updateDate": "2026-01-23T00:08:46Z",
    "updateDateIncludingText": "2026-01-23T00:08:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T17:54:44Z",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "WA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "WI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NJ"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "HI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CO"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "RI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MD"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1887is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1887\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Wyden (for himself, Ms. Cantwell , Mr. Merkley , Mr. Blumenthal , Ms. Baldwin , Mr. Van Hollen , Mr. Welch , Ms. Warren , Mr. Booker , Mr. Schatz , Mr. Bennet , Mr. Markey , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo amend the Help America Vote Act of 2002 to allow all eligible voters to vote by mail in Federal elections, to amend the National Voter Registration Act of 1993 to streamline the procedures under which individuals may apply to register to vote in such elections through State motor vehicle authorities, to permit automatic voter registration through such authorities for eligible citizens of the United States who do not complete voter registration applications, and for other purposes.\n#### 1. Short Title\nThis Act may be cited as the Vote at Home Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAn inequity of voting rights exists in the United States because voters in some States have the universal right to vote by mail while voters in other States do not.\n**(2)**\nMany voters often have work, family, or other commitments that make getting to polls and waiting in line on the date of an election difficult or impossible. Many citizens with disabilities are physically unable to vote due to long lines, inadequate parking, no curb cuts, steep ramps, and large crowds. In the 2022 election, the Election Assistance Commission found that 20 percent of voters with disabilities faced difficulties voting in person.\n**(3)**\nIn 2020, despite a global pandemic, the general election saw record high turnout as a result of increased vote by mail options, which allowed voters to cast a ballot and stay safe at the same time.\n**(4)**\nThirty-five States and the District of Columbia allow universal absentee voting (also known as no-excuse absentee voting), which permits any voter to request a mail-in ballot without providing a reason for the request. No State which has implemented no-excuse absentee voting has repealed it.\n**(5)**\nEight states and Washington, DC, conduct elections entirely by mail. At least 13 States currently allow some elections to be conducted by mail, especially in large and rural jurisdictions where voting by mail is especially convenient. Polling stations in rural jurisdictions tend to have higher costs per voter, smaller staffs, and limited resources. Transportation is often a crucial barrier for rural voters.\n**(6)**\nIn 2020, in order to provide greater accessibility and to protect the public health, 30 States adopted or changed their laws for the general election to allow voters to cast their ballots from home. These changes included removing strict excuse requirements or allowing COVID\u201319 concerns to be a valid excuse to vote absentee, allowing ballot drop boxes, offering prepaid postage on election mail, and proactively sending all active registered voters applications to request an absentee ballot, with some States even skipping that step and sending the actual ballots.\n**(7)**\nVoting by mail gives voters more time to consider their choices, which is especially important as many ballots contain greater numbers of questions about complex issues than in the past due to the expanded use of the initiative and referendum process in many States.\n**(8)**\nVoting by mail is cost effective. After the State of Oregon adopted vote-by-mail for all voters in 1996, the cost to administer an election in the State dropped by nearly 30 percent over the next few elections, from $3.07 per voter to $2.21 per voter. After Colorado implemented all-mail balloting in 2013, voting administration costs decreased by an average of 40 percent. The cost of conducting vote-by-mail elections is generally one-third to one-half less than conducting polling place elections. Voting by mail also saves a substantial amount by getting rid of the temporary labor costs of hiring poll workers. In addition to that cost, many jurisdictions have been facing difficulty in obtaining sufficient numbers of poll workers.\n**(9)**\nAllowing all voters the option to vote by mail can reduce waiting times for those voters who choose to vote at the polls. In 2024, voters in Illinois reported waiting in line up to 4 hours to vote; in Pennsylvania, voters reported waiting more than 6 hours to cast a ballot.\n**(10)**\nVoting by mail is preferable to many voters as an alternative to going to the polls. In 2024, nearly 30 percent of ballots in the United States were cast by mail, up from 10 percent in 2000. Voting by mail has become increasingly popular with voters who want to be certain that they are able to vote no matter what comes up on Election Day, as it reduces the physical obstacles and eases the time constraints connected with the act of voting.\n**(11)**\nDespite attempts to claim that voting by mail is susceptible to fraud, it is not. Strategies such as the tracking systems for ballots and Postal Service cooperation in preventing ballots from being delivered to names not recognized as receiving mail at an address nearly eliminate the potential for fraud in vote-by-mail elections. Evidence of undue influence or voter coercion after vote-by-mail implementation in Oregon has been nonexistent to minimal.\n**(12)**\nMany of the reasons which voters in many States are required to provide in order to vote by mail require the revelation of personal information about health, travel plans, or religious activities, which violate voters\u2019 privacy while doing nothing to prevent voter fraud.\n**(13)**\nState laws which require voters to obtain a notary signature to vote by mail only add cost and inconvenience to voters without increasing security.\n**(14)**\nVote-by-mail typically increases turnout in all elections, but can be particularly effective in increasing voter participation in special elections and primary elections. Oregon, Washington, and Colorado, 3 States with entirely vote-by-mail systems, continue to have consistently high voter turnout rates.\n**(15)**\nA crucial component of a modern voting system is making it easy, affordable, and accessible to register to vote. Twenty-four States and the District of Columbia have enacted automatic voter registration policies, with Oregon and California becoming the first to automatically register their citizens to vote when they apply for a driver\u2019s license. Automatic, permanent voter registration has the potential to increase participation, protect election integrity, and reduce registration costs.\n#### 3. Promoting ability of voters to vote by mail in Federal elections\n##### (a) Voting by mail in Federal elections\n**(1) In general**\nSubtitle A of title III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ) is amended by inserting after section 303 the following new section:\n303A. Promoting ability of voters to vote by mail (a) In General If an individual in a State is eligible to cast a vote in an election for Federal office, the State may not impose any additional conditions or requirements on the eligibility of the individual to cast the vote in such election by mail, except to the extent that the State imposes a deadline for requesting the ballot and related voting materials from the appropriate State or local election official and for returning the ballot to the appropriate State or local election official. (b) Provision of ballot materials Not later than 2 weeks before the date of any election for Federal office, each State shall mail ballots to individuals who are registered to vote in such election. (c) Accessibility for individuals with disabilities All ballots provided under this section shall be accessible to individuals with disabilities in a manner that provides the same opportunity for access and participation (including for privacy and independence) as for other voters. (d) Rule of construction Nothing in this section shall be construed to affect the authority of States to conduct elections for Federal office through the use of polling places at which individuals cast ballots. (e) Effective date A State shall be required to comply with the requirements of this section with respect to elections for Federal office held in years beginning with 2026. .\n**(2) Conforming amendment relating to enforcement**\nSection 401 of such Act ( 52 U.S.C. 21111 ) is amended by striking and 304 and inserting 303A, and 304 .\n**(3) Clerical Amendment**\nThe table of contents for such Act is amended by inserting after the item relating to section 303 the following new item:\nSec. 303A. Promoting ability of voters to vote by mail. .\n##### (b) Free postage for voting by mail\n**(1) In general**\nChapter 34 of title 39, United States Code, is amended by adding at the end the following:\n3407. Ballots provided for voting in Federal elections Blank ballots mailed pursuant to section 303A(b) of the Help America Vote Act of 2002 which are mailed by a State or local election official (individually or in bulk) to a voter, and voted ballots which are mailed by a voter to an election official, shall be carried expeditiously and free of postage. .\n**(2) Technical and conforming amendments**\n**(A) Table of sections**\nThe table of sections for chapter 34 of title 39, United States Code, is amended by adding at the end the following:\n3407. Ballots provided for voting in Federal elections. .\n**(B) Authorization of appropriations**\nSection 2401(c) of title 39, United States Code, is amended by striking 3403 through 3406 and inserting 3403 through 3407 .\n#### 4. Voter registration through State motor vehicle authorities\n##### (a) Streamlining existing procedures\nSection 5 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20504 ) is amended to read as follows:\n5. Voter registration through motor vehicle authority (a) Streamlined registration through application for driver\u2019s license (1) In general Each State shall include a voter registration application form for elections for Federal office as part of an application for a State motor vehicle driver\u2019s license for each applicable individual other than an applicable individual described in subsection (b)(1). (2) Forms and procedures The voter registration application portion of an application for a State motor vehicle driver's license\u2014 (A) may not require any information that duplicates information required in the driver's license portion of the form; (B) may require only the minimum amount of information necessary to\u2014 (i) prevent duplicate voter registrations; and (ii) enable State election officials to assess the eligibility of an applicable individual and to administer voter registration; (C) shall include a statement that\u2014 (i) states each eligibility requirement (including citizenship); (ii) contains an attestation that the applicant meets each such requirement; and (iii) requires the signature of the applicant, under penalty of perjury; (D) shall include\u2014 (i) a statement that, if an applicant declines to register to vote, the fact that the applicant has declined to register will remain confidential and will be used only for voter registration purposes; and (ii) a statement that if an applicant does register to vote, the office at which the applicant submits a voter registration application will remain confidential and will be used only for voter registration purposes; and (E) shall be made available (as submitted by the applicant, or in machine readable or other format) to the appropriate State election official as provided by State law\u2014 (i) subject to clause (ii), not later than 10 days after the date of acceptance; or (ii) if a registration application is accepted within 5 days before the last day for registration to vote in an election, not later than 5 days after the date of acceptance. (3) Treatment of attestations of eligibility For purposes of an application for voter registration with respect to elections for Federal office in a State under this subsection, an attestation of eligibility, including an attestation that the applicant is a United States citizen, shall be treated as the presumptive minimum amount of information necessary for the State to assess the eligibility of an applicable individual to vote in such elections and for the State to administer voter registration, except that a State shall prevent the completion of or reject the voter registration application of an applicable individual based upon reliable information in its possession demonstrating that the individual is not a United States citizen or is otherwise ineligible to register to vote in elections for Federal office in the State at the time of the application for a motor vehicle driver\u2019s license. (b) Automatic registration of eligible citizens (1) Duties of motor vehicle authority Each State motor vehicle authority shall transmit the voter registration information described in paragraph (2) with respect to an applicable individual to the appropriate election official if\u2014 (A) such individual has presented a document as part of an application for a State motor vehicle driver's license (including a document presented in a previous application retained by the State\u2019s motor vehicle authority) demonstrating that the individual is a United States citizen; or (B) based on information provided to the State motor vehicle authority by the appropriate election official, such individual is currently registered to vote in elections for Federal office in the State. (2) Voter registration information described The voter registration information transmitted by the State motor vehicle authority described in this paragraph is, with respect to an applicable individual, the minimum amount of information necessary to\u2014 (A) prevent duplicate voter registrations; (B) enable State election officials to assess the eligibility of such an individual who is not at that time registered to vote in elections for Federal office in the State and to administer voter registration; and (C) enable State election officials to update the address of such an individual who is currently registered to vote in elections for Federal office in the State. (3) Deadline for transmission to election official The voter registration information described in paragraph (2) shall be made available (in machine readable or other format) to the appropriate State election official as provided by State law\u2014 (A) subject to subparagraph (B), not later than 10 days after the date of acceptance; or (B) if the voter registration information is accepted within 5 days before the last day for registration to vote in an election, not later than 5 days after the date of acceptance. (4) Determination of registration status by election officials receiving information Upon receiving the voter registration information with respect to an individual under paragraph (1), the appropriate State election official shall determine\u2014 (A) whether such individual is at that time registered to vote in elections for Federal office in the State; (B) if the individual is at that time registered to vote in such elections, the address at which the individual is registered.; and (C) if the individual at that time is not registered to vote in elections for Federal office in the State, whether such individual is eligible to vote in such elections, including as provided by section 8(a)(3)(B) through the procedure set forth in section 303(a)(2)(A)(ii)(I) of the Help America Vote Act of 2002 ( 52 U.S.C. 21083(a)(2)(A)(ii)(I) ). (5) Registration of eligible unregistered individuals (A) Notice In the case of an applicable individual who is determined by the appropriate State election official to be eligible to vote in elections for Federal office in the State and who is not at the time registered to vote in such elections, the appropriate State election official shall issue a notice, which may be combined with the notice described in section 8(a)(2), to the individual containing\u2014 (i) a statement that the individual's records and signature shall constitute a completed registration for the individual unless the individual notifies the election official in response to the notice that the individual declines to be registered to vote in elections for Federal office held in the State; and (ii) a description of the process by which the individual may decline to be registered to vote in elections for Federal office in the State. (B) Registration Upon the issuance of a notice to an individual under subparagraph (A), the official shall ensure that the individual is registered to vote in elections for Federal office held in the State unless in response to the notice, the individual notifies the official that the individual declines to be registered to vote in such elections. (C) Removal of individuals incorrectly registered If, after an individual is registered under subparagraph (B) to vote in elections for Federal office held in the State, the appropriate State election official later determines that the individual does not meet the eligibility requirements for registering to vote in such elections, including as provided by section 8(a)(3)(B) or as a result of error relating to the duties of the State motor vehicle authority under paragraph (1), the individual shall be removed from the official list of registered voters in the State and deemed never to have registered to vote or attempted to register to vote. (6) Correcting addresses of individuals registered at different addresses (A) Notice In the case of an applicable individual who is registered to vote in elections for Federal office in the State at a different address in the State than the address provided in the information transmitted under this subsection, the appropriate State election official shall issue a notice, which may be combined with the notice described in section 8(a)(2), to the individual containing\u2014 (i) a statement that the address provided in such information shall be used as the individual's address for voter registration purposes; and (ii) a description of the process by which the individual may correct an address for voter registration purposes. (B) Change of address Upon the issuance of a notice to an individual under subparagraph (A), the official shall ensure that the individual is registered to vote in elections for Federal office at the address provided in the information transmitted under this subsection unless the individual corrects the change of address for voter registration purposes. (7) Voter protections (A) Protections for errors in registration An individual shall not be prosecuted under any Federal or State law, adversely affected in any civil adjudication concerning immigration status or naturalization, or subject to an allegation in any legal proceeding that the individual is not a citizen of the United States on any of the following grounds: (i) The individual notified an election office of the individual\u2019s automatic registration to vote under this subsection. (ii) The individual is not eligible to vote in elections for Federal office but was automatically registered to vote under this subsection due to agency error. (iii) The individual was automatically registered to vote under this subsection at an incorrect address. (iv) The individual did not make an affirmation of citizenship, including through automatic registration under this subsection. (B) Limits on use of automatic registration The automatic registration of any individual under this subsection or the fact that an individual did not make an affirmation of citizenship, including through automatic registration under this subsection, may not be used as evidence against that individual in any State or Federal law enforcement proceeding or any civil adjudication concerning immigration status or naturalization, and an individual\u2019s lack of knowledge or willfulness of such registration may be demonstrated by the individual\u2019s testimony alone. (C) Protection of election integrity Nothing in subparagraphs (A) or (B) may be construed to prohibit or restrict any action under color of law against an individual who\u2014 (i) knowingly and willfully makes a false statement to effectuate or perpetuate automatic voter registration under this subsection by any individual; or (ii) casts a ballot knowingly and willfully in violation of State law or the laws of the United States. (c) General provisions (1) Prohibiting transmission of information on noncitizens The State motor vehicle authority shall not transmit voter registration information under this section with respect to an applicable individual if, as part of the application for a State motor vehicle driver's license, the individual\u2014 (A) presents a document demonstrating that the individual is not a United States citizen at the time of the application; or (B) makes an attestation demonstrating that the individual is not a United States citizen at the time of the application, if such attestation is required by State law for purposes of the application for a State motor vehicle driver's license. (2) Limitation on use of information No information relating to the failure of an applicant for a State motor vehicle driver's license to sign a voter registration application or to an applicant\u2019s decision to decline voter registration may be used for any purpose other than voter registration. (3) Applicable individual For purposes of this section, the term applicable individual means any individual who submits an application for a State motor vehicle driver\u2019s license, including an initial application, renewal application, or change of address form, whether submitted in person, by mail, or by electronic means. .\n##### (b) Conforming Amendment Relating to Timing of Registration Prior to Elections\nSection 8(a)(1)(A) of such Act ( 52 U.S.C. 20507(a)(1)(A) ) is amended to read as follows:\n(A) in the case of registration through a motor vehicle authority under section 5\u2014 (i) if the valid voter registration form of the applicant is submitted to the motor vehicle authority under section 5(a), not later than the lesser of 30 days, or the period provided by State law, before the date of the election; or (ii) in the case of registration under section 5(b), if the voter registration information described in section 5(b)(2) which is transmitted by the motor vehicle authority is submitted by the applicant to the authority, not later than the lesser of 30 days, or the period provided by State law, before the date of the election; or .\n##### (c) Other Conforming Amendment\nSection 4(a)(1) of such Act ( 52 U.S.C. 20503(a)(1) ) is amended to read as follows:\n(1) through the State motor vehicle authority pursuant to section 5; .\n##### (d) Effective date\nThe amendments made by this section shall take effect upon the expiration of the 180-day period which begins on the date of the enactment of this Act.",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-04-10",
        "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2847",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Vote at Home Act of 2025",
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
        "updateDate": "2025-06-23T17:21:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-22",
    "originChamber": "Senate",
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
          "measure-id": "id119s1887",
          "measure-number": "1887",
          "measure-type": "s",
          "orig-publish-date": "2025-05-22",
          "originChamber": "SENATE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1887v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-05-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Vote at Home Act of 2025</strong></p><p>This bill expands voting by mail in federal elections and provides for automatic voter registration through state motor vehicle authorities.</p><p>Specifically, the bill prohibits states from imposing additional conditions or requirements on the eligibility of individuals to cast ballots by mail in federal elections, except states may impose a deadline for requesting the ballot and related voting materials and for returning a ballot.</p><p>Further, states must mail ballots to individuals registered to vote in a federal election not later than two weeks before the election.</p><p>In addition, the U.S. Postal Service must carry ballots for federal elections expeditiously and free of postage.</p><p>Finally, the bill provides for automatic voter registration of individuals through state motor vehicle authorities.</p>"
        },
        "title": "Vote at Home Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1887.xml",
    "summary": {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Vote at Home Act of 2025</strong></p><p>This bill expands voting by mail in federal elections and provides for automatic voter registration through state motor vehicle authorities.</p><p>Specifically, the bill prohibits states from imposing additional conditions or requirements on the eligibility of individuals to cast ballots by mail in federal elections, except states may impose a deadline for requesting the ballot and related voting materials and for returning a ballot.</p><p>Further, states must mail ballots to individuals registered to vote in a federal election not later than two weeks before the election.</p><p>In addition, the U.S. Postal Service must carry ballots for federal elections expeditiously and free of postage.</p><p>Finally, the bill provides for automatic voter registration of individuals through state motor vehicle authorities.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119s1887"
    },
    "title": "Vote at Home Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Vote at Home Act of 2025</strong></p><p>This bill expands voting by mail in federal elections and provides for automatic voter registration through state motor vehicle authorities.</p><p>Specifically, the bill prohibits states from imposing additional conditions or requirements on the eligibility of individuals to cast ballots by mail in federal elections, except states may impose a deadline for requesting the ballot and related voting materials and for returning a ballot.</p><p>Further, states must mail ballots to individuals registered to vote in a federal election not later than two weeks before the election.</p><p>In addition, the U.S. Postal Service must carry ballots for federal elections expeditiously and free of postage.</p><p>Finally, the bill provides for automatic voter registration of individuals through state motor vehicle authorities.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119s1887"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1887is.xml"
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
      "title": "Vote at Home Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-10T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Vote at Home Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Help America Vote Act of 2002 to allow all eligible voters to vote by mail in Federal elections, to amend the National Voter Registration Act of 1993 to streamline the procedures under which individuals may apply to register to vote in such elections through State motor vehicle authorities, to permit automatic voter registration through such authorities for eligible citizens of the United States who do not complete voter registration applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:53Z"
    }
  ]
}
```
