# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3191
- Title: Stop Ballroom Bribery Act
- Congress: 119
- Bill type: S
- Bill number: 3191
- Origin chamber: Senate
- Introduced date: 2025-11-18
- Update date: 2025-12-10T07:19:56Z
- Update date including text: 2025-12-10T07:19:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in Senate
- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-11-18: Introduced in Senate

## Actions

- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3191",
    "number": "3191",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Stop Ballroom Bribery Act",
    "type": "S",
    "updateDate": "2025-12-10T07:19:56Z",
    "updateDateIncludingText": "2025-12-10T07:19:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T22:50:58Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MD"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "IL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-12-08",
      "state": "NJ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3191is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3191\nIN THE SENATE OF THE UNITED STATES\nNovember 18, 2025 Ms. Warren (for herself, Mr. Blumenthal , Mr. Van Hollen , Mr. Schiff , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prevent corruption by appropriately limiting donations for any public property, building, or fixture at the White House, the Naval Observatory, or certain other public property, for events on such property, or for monuments to living current or former Presidents, current or former Vice Presidents, or current or former employees or officers appointed by the President.\n#### 1. Short title\nThis Act may be cited as the Stop Ballroom Bribery Act .\n#### 2. Donation restrictions for certain public property linked to President or Vice President\n##### (a) Definitions\nIn this section:\n**(1) Covered project**\nThe term covered project means\u2014\n**(A)**\nthe maintenance, acquisition, enhancement, improvement, alteration, demolition, or construction of any public property (including real property), building, or fixture located on or immediately adjacent to the grounds of the White House, the grounds of Number One Observatory Circle, or other public property intended for or dedicated to the use of the sitting President, the sitting Vice President, or a spouse or child of the sitting President or the sitting Vice President;\n**(B)**\nthe maintenance, acquisition, enhancement, improvement, alteration, demolition, or construction of a Federal monument or other structure on public property that names or honors a living current or former President, Vice President, or employee or officer appointed by the President; or\n**(C)**\nan event hosted on the grounds of the White House, the grounds of Number One Observatory Circle, or on any other public property intended for or dedicated to the use of the sitting President, the sitting Vice President, or a spouse or child of the sitting President or the sitting Vice President.\n**(2) Donation**\nThe term donation means a gift, donation, bequest, or devise of anything of value, including services, whether made directly to the Federal Government or indirectly via another entity or person.\n**(3) Foreign government**\nThe term foreign government has the meaning given that term in section 7342 of title 5, United States Code.\n**(4) Lobbying activities**\nThe term lobbying activities has the meaning given that term in section 3 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602 ).\n**(5) Nonprofit organization**\nThe term nonprofit organization means an organization that is described in paragraph (3) or (4) of section 501(c) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code.\n##### (b) Restrictions on accepting donations\n**(1) NPS and OGE approval before acceptance or use of a donation for a covered project**\nA donation for a covered project may be accepted or used by the Federal Government only\u2014\n**(A)**\nin accordance with an authority to accept gifts or reimbursements under existing law; and\n**(B)**\nif the individual who is serving in the position of Director of the National Park Service, and who has been appointed to such position by the President, by and with the advice and consent of the Senate\u2014\n**(i)**\nmakes a written determination, with the concurrence of the individual who is serving in the position of Director of the Office of Government Ethics, and who has been appointed to such position by the President, by and with the advice and consent of the Senate, that the donation complies with the restrictions under paragraph (2);\n**(ii)**\nsubmits to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives the determination described in clause (i); and\n**(iii)**\npublishes the determination described in clause (i) in the Federal Register.\n**(2) Restrictions; requirements for donors**\n**(A) Prohibited donations**\nA donation for a covered project may not be accepted or used by an officer or employee of the United States, including the President and Vice President, or a non-Governmental agent operating on behalf of such an officer or employee, if the ultimate source of the donation, in part or in whole, is a person who\u2014\n**(i)**\nat the time the donation is made is, or at any time on or after the date on which the sitting President assumed the office of President was, involved in litigation with the Federal Government;\n**(ii)**\nat the time the donation is made is, or at any time on or after the date on which the sitting President assumed the office of President was, the subject or target of an administrative investigation or other enforcement action by the Federal Government;\n**(iii)**\nat the time the donation is made is seeking or has in effect a contract or other business relationship with the Federal Government;\n**(iv)**\nat the time the donation is made is seeking a grant from the Federal Government or has received such grant for which the funds have not been fully expended, revoked, or depleted;\n**(v)**\nat the time the donation is made is, or at any time on or after the date on which the sitting President assumed the office of President was, involved in lobbying activities targeting any part of the executive branch;\n**(vi)**\nat the time the donation is made is seeking or requesting, or at any time on or after the date on which the sitting President assumed the office of President sought, requested, or received, a pardon from the President; or\n**(vii)**\nat the time the donation is made is seeking, or at any time on or after the date on which the sitting President assumed the office of President sought, to be appointed to a position in the Federal Government by the President.\n**(B) Integrity of donation**\nA donation for a covered project may not be accepted or used if the donation\u2014\n**(i)**\nincludes as an actual or implied condition of receipt of the donation any benefit derived from the Federal Government;\n**(ii)**\nhas been coerced through the use of the authority or position of any officer or employee of the United States, including the President or the Vice President; or\n**(iii)**\nwould influence or appear to influence the performance of the responsibilities by any officer or employee of the executive branch of the Federal Government, including the President or Vice President, or would otherwise compromise the integrity or appearance of integrity of any part of the executive branch of the Federal Government.\n**(C) Prohibited solicitation**\nAn officer or employee of the Executive Office of the President, including the President and Vice President, or the spouse or child of the President or Vice President, may not solicit a donation for a covered project.\n**(D) Approval of foreign gifts and emoluments**\nA donation for a covered project made by a foreign government may not be accepted unless Congress has approved the accepting of the donation.\n##### (c) Post-Donation restrictions\n**(1) Donor recognition limitations**\nA donor name, donor logo, or other indication of the identity of a donor may not be displayed at any location described in subsection (a)(1) as recognition of the donation.\n**(2) Cooling-off period**\nA person making a donation for a covered project may not engage in any lobbying activities directed at any officer or employee of the United States in a position in the executive branch, including the President or the Vice President, during the 2-year period beginning on the date of the donation.\n**(3) Conversion of donation to personal use**\nNo person may convert a donation to a covered project to the private use of the person, or to the personal use of any other person.\n**(4) Disposition of leftover donations**\nIn addition to any other restriction on the disposition of unused funds by a nonprofit organization or other entity or person, the remaining balances of a donation for a covered project may not be expended for anything that directly and predictably benefits the President, the Vice President, a spouse or child of the President or the Vice President, an employee of the Executive Office of the President, or any officer appointed by the President.\n##### (d) Transparency To ensure donations are disclosed and prohibit straw donations\n**(1) Disclosing donor meetings**\n**(A) In general**\nIn accordance with subparagraph (B), a person making a donation to or for the benefit of a covered project, directly or indirectly through another person, shall disclose to the Director of the National Park Service any meeting or other communication with the President, the Vice President, a spouse or child of the President or the Vice President, any other officer or employee of the United States, or any agent working on any of their behalf that occurs during the period beginning on the date that is 1 year before the date of the donation and ending on the date that is 1 year after the date of the donation, and the disclosure shall, for each such meeting, include the topics discussed and the date of the meeting.\n**(B) Timing of disclosure**\nA person required to disclose a meeting or other communication under subparagraph (A) shall\u2014\n**(i)**\nwith respect to a meeting or other communication occurring before the date of the applicable donation, make the disclosure required under subparagraph (A) not later than 7 days after the date of the donation; or\n**(ii)**\nwith respect to a meeting or other communication occurring on or after the date of the applicable donation, make the disclosure required under subparagraph (A) not later than 7 days after the meeting or other communication.\n**(2) Quarterly publication**\nThe Director of the National Park Service, in coordination with the heads of any other relevant agencies and entities, shall publish a quarterly report in the Federal Register listing each donation contributed to or for the benefit of a covered project, which shall include, for each donation\u2014\n**(A)**\na brief description of the donation and the circumstances justifying acceptance;\n**(B)**\nthe date of acceptance;\n**(C)**\nthe identity of each person who\u2014\n**(i)**\ncontributed to the donation; and\n**(ii)**\ncontributed an aggregate amount of more than $200 as a part of donations made during the applicable calendar quarter; and\n**(D)**\ninformation regarding any meeting or other communication described in paragraph (1).\n**(3) Prohibition on straw donations**\nWith respect to any donation to a covered project, whether made directly or indirectly, it shall be unlawful for a person to knowingly\u2014\n**(A)**\nmake the donation in the name of another person;\n**(B)**\npermit the name of that person to be used to effect the donation by another person;\n**(C)**\naccept such a donation that is made by one person in the name of another person; or\n**(D)**\ndirect, help, or assist any person in making such a donation in the name of another person.\n**(4) Prohibition on anonymous donations**\nNo donation for a covered project may be accepted if it is made on the condition that it be anonymous.\n**(5) Attestation by certain donors**\nA donor employed by or closely affiliated with a person barred from making a donation under subsection (b)(2)(A) shall attest that the donor is not explicitly or implicitly making the donation on behalf of the person.\n##### (e) Enforcement\n**(1) OGE regulations and disgorgement**\nNot later than 180 days after the date of enactment of this Act, the Director of the Office of Government Ethics shall publish regulations implementing the procedures under this section, which shall permit the Director to direct the return of any donation that violates any provision of this section at any point in time.\n**(2) Judicial review of OGE determinations**\nAny determination by the Director of the Office of Government Ethics under this section shall be subject to judicial review and the attorney general of a State or the Attorney General may bring an action in accordance with this subsection seeking judicial review of such a determination.\n**(3) Enforcement by State attorneys general**\nThe attorney general of a State may bring a civil action to redress a violation of this section in the United States District Court for the District of Columbia or in any district court of the United States with jurisdiction over any part of the United States served by that attorney general.\n**(4) Enforcement by the United States**\nThe Attorney General of the United States may bring a civil action or criminal prosecution to redress a violation of this section in the United States District Court for the District of Columbia.\n**(5) Civil and criminal penalties**\n**(A) Civil**\n**(i) In general**\nSubject to clause (ii), any person who violates this section shall be subject to\u2014\n**(I)**\na civil penalty that does not exceed the greater of $20,000 or an amount equal to the aggregate value of the donations involved in such violation; and\n**(II)**\nan order requiring the person to disgorge any benefit derived from any donation involved in the violation.\n**(ii) Larger violations**\nIf the aggregate value of all donations involved in a violation of this section by a person during a calendar year exceeds $50,000, the person shall be subject to\u2014\n**(I)**\na civil penalty that does not exceed the greater of $100,000 or the amount equal to the aggregate value of the donations involved in such violation; and\n**(II)**\nan order requiring the person to disgorge any benefit derived from any donation involved in the violation.\n**(B) Criminal**\n**(i) In general**\nSubject to clause (ii), any person who knowingly and willfully violates this section shall be\u2014\n**(I)**\nfined under title 18, United States Code, imprisoned for not more than 1 year, or both; and\n**(II)**\nsubject to an order requiring the person to disgorge any benefit derived from any donation involved in the violation.\n**(ii) Larger violations**\nIf the aggregate value of all donations involved in a violation of this section by a person during a calendar year exceeds $50,000, the person shall be\u2014\n**(I)**\nfined under title 18, United States Code, imprisoned for not more than 5 years, or both; and\n**(II)**\nsubject to an order requiring the person to disgorge any benefit derived from any donation involved in the violation.\n**(6) Other relief**\nIn addition to the civil and criminal penalties described in paragraph (5), in an action brought under this subsection a court may grant a permanent or temporary injunction, restraining order, or other order, upon a showing that the person involved has likely committed a violation of this section.\n**(7) Period of limitations**\n**(A) Civil**\nA civil action under this subsection may not be commenced later than 10 years after the cause of action accrues.\n**(B) Criminal**\nNo person shall be prosecuted, tried, or punished for any offense under this subsection, unless the indictment is found or the information is instituted within 10 years after such offense shall have been committed.\n**(8) Rule of construction**\nThe imposition of a civil or criminal penalty under this subsection does not preclude any other criminal or civil statutory, common law, or administrative remedy, which is available by law to the United States or any other person.\n##### (f) Severability\nIf any provision of this section, or the application of a provision of this section to any person or circumstance, is held to be unconstitutional, the remainder of this section, and the application of the provision to any other person or circumstance, shall not be affected thereby.",
      "versionDate": "2025-11-18",
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
        "actionDate": "2025-11-18",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committees on Natural Resources, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6085",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Ballroom Bribery Act",
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
        "updateDate": "2025-12-02T19:52:50Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3191is.xml"
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
      "title": "Stop Ballroom Bribery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Ballroom Bribery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prevent corruption by appropriately limiting donations for any public property, building, or fixture at the White House, the Naval Observatory, or certain other public property, for events on such property, or for monuments to living current or former Presidents, current or former Vice Presidents, or current or former employees or officers appointed by the President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-26T05:33:20Z"
    }
  ]
}
```
