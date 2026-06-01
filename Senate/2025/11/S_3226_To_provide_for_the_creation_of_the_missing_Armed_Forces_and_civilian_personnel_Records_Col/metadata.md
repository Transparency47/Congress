# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3226?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3226
- Title: Bring Our Heroes Home Act
- Congress: 119
- Bill type: S
- Bill number: 3226
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2026-04-20T21:15:13Z
- Update date including text: 2026-04-20T21:15:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3226",
    "number": "3226",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Bring Our Heroes Home Act",
    "type": "S",
    "updateDate": "2026-04-20T21:15:13Z",
    "updateDateIncludingText": "2026-04-20T21:15:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
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
            "date": "2025-11-19T23:59:08Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-19T23:59:08Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NH"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "ID"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NV"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NH"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "HI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "HI"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3226is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3226\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Crapo (for himself, Mrs. Shaheen , Mr. Risch , Mr. Padilla , Ms. Klobuchar , Ms. Duckworth , Ms. Rosen , Ms. Hassan , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo provide for the creation of the missing Armed Forces and civilian personnel Records Collection at the National Archives, to require the expeditious public transmission to the Archivist and public disclosure of missing Armed Forces and civilian personnel records, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bring Our Heroes Home Act .\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds that all records of the Federal Government relating to missing Armed Forces and civilian personnel should\u2014\n**(1)**\nbe preserved for historical and governmental purposes and for public research, including for families seeking to learn the ultimate fate of their loved ones;\n**(2)**\ncarry a presumption of declassification; and\n**(3)**\nbe disclosed under this Act to enable the fullest possible accounting for missing Armed Forces and civilian personnel.\n##### (b) Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto provide for the creation of the Missing Armed Forces and Civilian Personnel Records Collection at the National Archives; and\n**(2)**\nto require the expeditious public transmission to the Archivist and public disclosure of missing Armed Forces and civilian personnel records, subject to narrow exceptions, as set forth in this Act.\n#### 3. Definitions\nIn this Act:\n**(1) Archivist**\nThe term Archivist means the Archivist of the United States.\n**(2) Collection**\nThe term Collection means the Missing Armed Forces and Civilian Personnel Records Collection established under section 4(a).\n**(3) Executive agency**\nThe term Executive agency \u2014\n**(A)**\nmeans an agency, as defined in section 552(f) of title 5, United States Code;\n**(B)**\nincludes any Executive department, military department, Government corporation, Government controlled corporation, or other establishment in the executive branch of the Federal Government, including the Executive Office of the President, any branch of the Armed Forces, and any independent regulatory agency; and\n**(C)**\ndoes not include any non-appropriated agency, department, corporation, or establishment.\n**(4) Executive Director**\nThe term Executive Director means the Executive Director of the Review Board.\n**(5) Government office**\nThe term Government office means an Executive agency, the Library of Congress, or the National Archives.\n**(6) Missing Armed Forces and civilian personnel**\nThe term missing Armed Forces and civilian personnel \u2014\n**(A)**\nmeans 1 or more missing persons; and\n**(B)**\nincludes an individual who was a missing person and whose status was later changed to missing and presumed dead .\n**(7) Missing Armed Forces and civilian personnel record**\nThe term missing Armed Forces and civilian personnel record means a record that relates, directly or indirectly, to the loss, fate, or status of missing Armed Forces and civilian personnel that\u2014\n**(A)**\nwas created or made available for use by, obtained by, or otherwise came into the custody, possession, or control of\u2014\n**(i)**\nany Government office;\n**(ii)**\nany Presidential library; or\n**(iii)**\nany of the Armed Forces; and\n**(B)**\nrelates to 1 or more missing Armed Forces and civilian personnel who became missing persons during the period\u2014\n**(i)**\nbeginning on December 7, 1941; and\n**(ii)**\nending on the date of enactment of this Act.\n**(8) Missing person**\nThe term missing person means\u2014\n**(A)**\na person described in paragraph (1) of section 1513 of title 10, United States Code; and\n**(B)**\nany other civilian employee of the Federal Government or an employee of a contractor of the Federal Government who serves in direct support of, or accompanies, the Armed Forces in the field under orders and who is in a missing status (as that term is defined in paragraph (2) of such section 1513).\n**(9) National Archives**\nThe term National Archives \u2014\n**(A)**\nmeans the National Archives and Records Administration; and\n**(B)**\nincludes any component of the National Archives and Records Administration (including Presidential archival depositories established under section 2112 of title 44, United States Code).\n**(10) Official investigation**\nThe term official investigation means a review, briefing, inquiry, or hearing relating to missing Armed Forces and civilian personnel conducted by a Presidential commission, committee of Congress, or agency, regardless of whether it is conducted independently, at the request of any Presidential commission or committee of Congress, or at the request of any official of the Federal Government.\n**(11) Originating body**\nThe term originating body means the Government office or other initial source that created a record or particular information within a record.\n**(12) Public interest**\nThe term public interest means the compelling interest in the prompt public disclosure of missing Armed Forces and civilian personnel records for historical and governmental purposes, for public research, and for the purpose of fully informing the people of the United States, most importantly families of missing Armed Forces and civilian personnel, about the fate of the missing Armed Forces and civilian personnel and the process by which the Federal Government has sought to account for them.\n**(13) Record**\nThe term record has the meaning given the term records in section 3301 of title 44, United States Code.\n**(14) Review Board**\nThe term Review Board means the Missing Armed Forces and Civilian Personnel Records Review Board established under section 5.\n#### 4. Missing Armed Forces and Civilian Personnel Records Collection at the National Archives\n##### (a) Establishment of collection\nNot later than 90 days after a quorum of the Missing Armed Forces and Civilian Personnel Records Review Board has been established under section 7, the Archivist shall\u2014\n**(1)**\ncommence establishment of a collection of records to be known as the Missing Armed Forces and Civilian Personnel Records Collection ;\n**(2)**\ncommence preparing the subject guidebook and index to the Collection; and\n**(3)**\nestablish criteria and acceptable formats for Executive agencies to follow when transmitting copies of missing Armed Forces and civilian personnel records to the Archivist, to include required metadata, including applicable information privacy safeguards.\n##### (b) Regulations\nNot later than 90 days after the date of the swearing in of the Review Board members, the Review Board shall promulgate rules to establish guidelines and processes for the disclosure of records contained in the Collection, including applicable information privacy safeguards.\n##### (c) Oversight\n**(1) Senate**\nThe Committee on Homeland Security and Governmental Affairs of the Senate shall have continuing jurisdiction, including legislative oversight jurisdiction, in the Senate with respect to the Collection.\n**(2) House of Representatives**\nThe Committee on Oversight and Government Reform of the House of Representatives shall have continuing jurisdiction, including legislative oversight jurisdiction, in the House of Representatives with respect to the Collection.\n#### 5. Review, identification, transmission to the National Archives, and public disclosure of missing Armed Forces and civilian personnel records by Government offices\n##### (a) In general\n**(1) Preparation**\nAs soon as practicable after the date of enactment of this Act, and sufficiently in advance of the deadlines established under this Act, each Government office shall\u2014\n**(A)**\nidentify and locate any missing Armed Forces and civilian personnel records in the custody, possession, or control of the Government office, including intelligence reports, congressional inquiries, memoranda to or from the White House and other Federal departments and agencies, Prisoner of War (POW) debriefings, live sighting reports, documents relating to POW camps, movement of POWs, exploitation of POWs, experimentation on POWs, or status changes from Missing in Action (MIA) to Killed in Action (KIA); and\n**(B)**\nprepare for transmission to the Archivist in accordance with the criteria and acceptable formats established by the Archivist a copy of any missing Armed Forces and civilian personnel records that have not previously been transmitted to the Archivist by the Government office.\n**(2) Certification**\nEach Government office shall submit to the Archivist, under penalty of perjury, a certification indicating\u2014\n**(A)**\nwhether the Government office has conducted a thorough search for all missing Armed Forces and civilian personnel records in the custody, possession, or control of the Government office; and\n**(B)**\nwhether a copy of any missing Armed Forces and civilian personnel record has not been transmitted to the Archivist.\n**(3) Preservation**\nNo missing Armed Forces and civilian personnel record shall be destroyed, altered, or mutilated in any way.\n**(4) Effect of previous disclosure**\nInformation that was made available or disclosed to the public before the date of enactment of this Act in a missing Armed Forces and civilian personnel record may not be withheld, redacted, postponed for public disclosure, or reclassified.\n**(5) Withheld and substantially redacted records**\n**(A) In general**\nFor any missing Armed Forces and civilian personnel record that is transmitted to the Archivist which a Government office proposes to substantially redact or withhold in full from public access, the head of the Government office shall submit an unclassified and publicly releasable report to the Archivist, the Review Board, and each appropriate committee of the Senate and the House of Representatives justifying the decision of the Government office to substantially redact or withhold the record by demonstrating that the release of information would clearly and demonstrably be expected to cause an articulated harm, and that the harm would be of such gravity as to outweigh the public interest in access to the information.\n**(B) Rulemaking**\nThe Archivist shall promulgate regulations to define the term substantially redacted record for purposes of subparagraph (A).\n##### (b) Review\n**(1) In general**\nExcept as provided under paragraph (5), not later than 270 days after a quorum of the Review Board has been established under section 7, each Government office shall, in accordance with the criteria and acceptable formats established by the Archivist\u2014\n**(A)**\nidentify, locate, copy, and review each missing Armed Forces and civilian personnel record in the custody, possession, or control of the Government office for transmission to the Archivist and disclosure to the public or, if needed, review by the Review Board; and\n**(B)**\ncooperate fully, in consultation with the Archivist, in carrying out paragraph (3).\n**(2) Requirement**\nThe Review Board shall promulgate rules for the disclosure of relevant records by Government offices under paragraph (1).\n**(3) National Archives records**\nNot later than 270 days after a quorum of the Review Board has been established under section 7, the Archivist shall\u2014\n**(A)**\nlocate and identify all missing Armed Forces and civilian personnel records in the custody of the National Archives as of the date of enactment of this Act that remain classified, in whole or in part;\n**(B)**\nnotify a Government office if the Archivist locates and identifies a record of the Government office under subparagraph (A); and\n**(C)**\nmake each classified missing Armed Forces and civilian personnel record located and identified under subparagraph (A) available for review by Executive agencies through the National Declassification Center established under Executive Order 13526 ( 50 U.S.C. 3161 note; relating to classified national security information), or any successor order.\n**(4) Records already public**\nA missing Armed Forces and civilian personnel record that is in the custody of the National Archives on the date of enactment of this Act and that has been publicly available in its entirety without redaction shall be made available in the Collection without any additional review by the Archivist, the Review Board, or any other Government office under this Act.\n**(5) Exemptions**\n**(A) Department of Defense POW/MIA Accounting Agency**\nThe Defense POW/MIA Accounting Agency is exempt from the requirement under this subsection to declassify and transmit to the Archivist documents in its custody or control that pertain to a specific case or cases that the Defense POW/MIA Accounting Agency is actively investigating or developing for the purpose of locating, disinterring, or identifying a missing member of the Armed Forces.\n**(B) Department of Defense Military Service Casualty Offices and Department of State Service Casualty Offices**\nThe Department of Defense Military Service Casualty Offices and the Department of State Service Casualty Offices are exempt from the requirement to declassify and transmit to the Archivist documents in their custody or control that pertain to individual cases with respect to which the office is lending support and assistance to the families of missing individuals.\n##### (c) Transmission to the National Archives\nEach Government office shall\u2014\n**(1)**\nnot later than 270 days after a quorum of the Review Board has been established under section 7, commence transmission to the Archivist of copies of the missing Armed Forces and civilian personnel records in the custody, possession, or control of the Government office, except for records described in subsection (a)(5); and\n**(2)**\nnot later than 1 year after a quorum of the Review Board has been established under section 7, complete transmission to the Archivist of copies of all missing Armed Forces and civilian personnel records in the possession or control of the Government office.\n##### (d) Periodic review of postponed missing Armed Forces and civilian personnel records\n**(1) In general**\nAll missing Armed Forces and civilian personnel records, or information within a missing Armed Forces and civilian personnel record, the public disclosure of which has been postponed under the standards under this Act shall be reviewed by the originating body\u2014\n**(A)**\n**(i)**\nperiodically, but not less than every 5 years, after the date on which the Review Board terminates under section 7(p); and\n**(ii)**\nat the direction of the Archivist; and\n**(B)**\nconsistent with the recommendations of the Review Board under section 9(b)(3)(B).\n**(2) Contents**\n**(A) In general**\nA periodic review of a missing Armed Forces and civilian personnel record, or information within a missing Armed Forces and civilian personnel record, by the originating body shall address the public disclosure of the missing Armed Forces and civilian personnel record under the standards under this Act.\n**(B) Continued postponement**\nIf an originating body conducting a periodic review of a missing Armed Forces and civilian personnel record, or information within a missing Armed Forces and civilian personnel record, the public disclosure of which has been postponed under the standards under this Act, determines that continued postponement is required, the originating body shall provide to the Archivist an unclassified written description of the reason for the continued postponement that the Archivist shall highlight and make accessible on a publicly accessible website administered by the National Archives.\n**(C) Scope**\nThe periodic review of postponed missing Armed Forces and civilian personnel records, or information within a missing Armed Forces and civilian personnel record, shall serve the purpose stated in section 2(b)(2), to provide expeditious public disclosure of missing Armed Forces and civilian personnel records, to the fullest extent possible, subject only to the grounds for postponement of disclosure under section 6.\n**(D) Disclosure absent certification by President**\nNot later than 10 years after the date on which a quorum of the Review Board has been established under section 7, all missing Armed Forces and civilian personnel records, and information within a missing Armed Forces and civilian personnel record, shall be publicly disclosed in full, and available in the Collection, unless\u2014\n**(i)**\nthe head of the originating body, Executive agency, or other Government office recommends in writing that continued postponement is necessary;\n**(ii)**\nthe written recommendation described in clause (i)\u2014\n**(I)**\nis provided to the Archivist in unclassified and publicly releasable form not later than 180 days before the date that is 10 years the date on which a quorum of the Review Board has been established under section 7; and\n**(II)**\nincludes\u2014\n**(aa)**\na justification of the recommendation to postpone disclosure with clear and convincing evidence that the identifiable harm is of such gravity that it outweighs the public interest in disclosure; and\n**(bb)**\na recommended specified time at which or a specified occurrence following which the material may be appropriately disclosed to the public under this Act;\n**(iii)**\nthe Archivist transmits all recommended postponements and the recommendation of the Archivist to the President not later than 90 days before the date that is 10 years after the date on which a quorum of the Review Board has been established under section 7; and\n**(iv)**\nthe President transmits to the Archivist a certification indicating that continued postponement is necessary and the identifiable harm, as demonstrated by clear and convincing evidence, is of such gravity that it outweighs the public interest in disclosure not later than the date that is 10 years after the date on which a quorum of the Review Board has been established under section 7.\n##### (e) Records management\nIn carrying out this section, the Archivist shall comply with any applicable statutory or regulatory requirement related to records management.\n#### 6. Grounds for postponement of public disclosure of records\n##### (a) In general\nDisclosure to the public of a missing Armed Forces and civilian personnel record or particular information in a missing Armed Forces and civilian personnel record created after the date that is 25 years before the date of the review of the missing Armed Forces and civilian personnel record by the Archivist may be postponed subject to the limitations under this Act only\u2014\n**(1)**\nif\u2014\n**(A)**\nit pertains to\u2014\n**(i)**\nmilitary plans, weapons systems, or operations;\n**(ii)**\nforeign government information;\n**(iii)**\nintelligence activities (including covert action), intelligence sources or methods, or cryptology;\n**(iv)**\nforeign relations or foreign activities of the United States, including confidential sources;\n**(v)**\nscientific, technological, or economic matters relating to the national security;\n**(vi)**\nUnited States Government programs for safeguarding nuclear materials or facilities;\n**(vii)**\nvulnerabilities or capabilities of systems, installations, infrastructures, projects, plans, or protection services relating to the national security; or\n**(viii)**\nthe development, production, or use of weapons of mass destruction; and\n**(B)**\nthe threat posed by the public disclosure of the missing Armed Forces and civilian personnel record or information is of such gravity that it outweighs the public interest in disclosure;\n**(2)**\nif the information is protected from disclosure under section 552(b) of title 5, United States Code (commonly known as the Freedom of Information Act ); or\n**(3)**\nif it reveals information described in paragraphs (1) through (9) of section 3.3(b) of Executive Order 13526 ( 50 U.S.C. 3161 note; relating to classified national security information).\n##### (b) Older records\nDisclosure to the public of a missing Armed Forces and civilian personnel record or particular information in a missing Armed Forces and civilian personnel record created on or before the date that is 25 years before the date of the review of the missing Armed Forces and civilian personnel record by the Archivist may be postponed subject to the limitations under this Act only if, as demonstrated by clear and convincing evidence\u2014\n**(1)**\nthe release of the information would be expected to\u2014\n**(A)**\nreveal the identity of a confidential human source, a human intelligence source, a relationship with an intelligence or security service of a foreign government or international organization, or a nonhuman intelligence source, or impair the effectiveness of an intelligence method currently in use, available for use, or under development;\n**(B)**\nreveal information that would impair United States cryptologic systems or activities;\n**(C)**\nreveal formally named or numbered United States military war plans that remain in effect, or reveal operational or tactical elements of prior plans that are contained in such active plans; or\n**(D)**\nreveal information, including foreign government information, that would cause serious harm to relations between the United States and a foreign government, or to ongoing diplomatic activities of the United States; and\n**(2)**\nthe threat posed by the public disclosure of the missing Armed Forces and civilian personnel record or information is of such gravity that it outweighs the public interest in disclosure.\n##### (c) Exception\nRegardless of the date on which a missing Armed Forces and civilian personnel record was created, disclosure to the public of information in the missing Armed Forces and civilian personnel record may be postponed if\u2014\n**(1)**\nthe public disclosure of the information would reveal the name or identity of a living person who provided confidential information to the United States and would pose a substantial risk of harm to that person, in accordance with section 552(b)(7)(D) of title 5, United States Code;\n**(2)**\nthe public disclosure of the information could reasonably be expected to constitute an unwarranted invasion of personal privacy, and that invasion of privacy is so substantial that it outweighs the public interest;\n**(3)**\nthe public disclosure of the information could reasonably be expected to cause harm to the methods currently in use or available for use by members of the Armed Forces to survive, evade, resist, or escape; or\n**(4)**\nthe public disclosure of such information would conflict with United States law, regulations, or executive orders, including any law, regulation, or executive order governing the disclosure of classified information.\n#### 7. Establishment and powers of the Missing Armed Forces and Civilian Personnel Records Review Board\n##### (a) Establishment\nThere is established as an independent establishment in the executive branch a board to be known as the Missing Armed Forces and Civilian Personnel Records Review Board to ensure and facilitate the review, transmission to the Archivist, and public disclosure of missing Armed Forces and civilian personnel records.\n##### (b) Membership\n**(1) Appointments**\nThe Review Board shall be composed of 5 members appointed by the President, subject to the advice and consent of the Senate, of whom\u2014\n**(A)**\n1 shall be appointed in consultation with the Archivist of the United States and shall serve as the Chairperson of the Review Board;\n**(B)**\n1 shall be appointed in consultation with the majority leader of the Senate;\n**(C)**\n1 shall be appointed in consultation with the minority leader of the Senate;\n**(D)**\n1 shall be appointed in consultation with the Speaker of the House of Representatives; and\n**(E)**\n1 shall be appointed in consultation with the minority leader of the House of Representatives.\n**(2) Qualifications**\nThe members of the Review Board shall\u2014\n**(A)**\nbe appointed without regard to political affiliation;\n**(B)**\nbe citizens of the United States of integrity and impartiality;\n**(C)**\nnot be employees of an Executive agency on the date of the appointment;\n**(D)**\nhave high national professional reputation in their fields and be capable of exercising the independent and objective judgment necessary to the fulfillment of their role in ensuring and facilitating the identification, location, review, transmission to the Archivist, and public disclosure of missing Armed Forces and civilian personnel records;\n**(E)**\npossess an appreciation of the value of missing Armed Forces and civilian personnel records to scholars, the Federal Government, and the public, particularly families of missing Armed Forces and civilian personnel;\n**(F)**\ninclude at least 1 professional historian; and\n**(G)**\ninclude at least 1 attorney.\n**(3) Consultation with the Office of Government Ethics**\nIn considering persons to be appointed to the Review Board, the President shall consult with the Director of the Office of Government Ethics to\u2014\n**(A)**\ndetermine criteria for possible conflicts of interest of members of the Review Board, consistent with ethics laws, statutes, and regulations for executive branch employees; and\n**(B)**\nensure that no individual selected for such position of member of the Review Board possesses a conflict of interest as so determined.\n**(4) Consultation**\nAppointments to the Review Board shall be made after considering individuals recommended by the American Historical Association, the Organization of American Historians, the Society of American Archivists, the American Bar Association, veterans\u2019 organizations, and organizations representing families of missing Armed Forces and civilian personnel.\n##### (c) Security clearances\n**(1) In general**\nEach member of the Review Board shall seek appropriate security clearances necessary to carry out the duties of the Review Board.\n**(2) Review**\nThe appropriate departments, agencies, and elements of the executive branch of the Federal Government shall cooperate to ensure that an application by an individual nominated to be a member of the Review Board seeking a security clearance under paragraph (1) is expeditiously reviewed and granted or denied.\n##### (d) Consideration by the Senate\nNominations for appointment under subsection (b)(1)(A) shall be referred to the Committee on Homeland Security and Governmental Affairs of the Senate for consideration.\n##### (e) Vacancy\nNot later than 60 days after the date on which a vacancy on the Review Board occurs, the vacancy shall be filled in the same manner as specified for original appointment.\n##### (f) Chairperson needed for quorum\nA majority of the members of the Review Board, including the Chairperson appointed and confirmed pursuant to subsection (b)(1)(A), shall constitute a quorum.\n##### (g) Removal of Review Board member\n**(1) In general**\nA member of the Review Board shall not be removed from office, other than\u2014\n**(A)**\nby impeachment by Congress; or\n**(B)**\nby the action of the President for inefficiency, neglect of duty, malfeasance in office, physical disability, mental incapacity, or any other condition that substantially impairs the performance of the member\u2019s duties.\n**(2) Judicial review**\n**(A) In general**\nA member of the Review Board removed from office may obtain judicial review of the removal in a civil action commenced in the United States District Court for the District of Columbia.\n**(B) Relief**\nThe member may be reinstated or granted other appropriate relief by order of the court.\n**(3) Notice of removal**\nIf a member of the Review Board is removed from office, and that removal is by the President, not later than 10 days after the removal, the President shall submit to the leadership of Congress, the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Reform of the House of Representatives a report specifying the facts found and the grounds for the removal.\n##### (h) Compensation of members\n**(1) Basic pay**\nA member of the Review Board shall be treated as an employee of the executive branch and compensated at a rate equal to the daily equivalent of the annual rate of basic pay prescribed for level IV of the Executive Schedule under section 5315 of title 5, United States Code, for each day, including travel time, during which the member is engaged in the performance of the duties of the Review Board.\n**(2) Travel expenses**\nA member of the Review Board shall be allowed reasonable travel expenses, including per diem in lieu of subsistence, at rates for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from the member\u2019s home or regular place of business in the performance of services for the Review Board.\n##### (i) Duties of the Review Board\n**(1) In general**\nThe Review Board shall consider and render a decision on a determination by a Government office to seek to postpone the disclosure of a missing Armed Forces and civilian personnel record, in whole or in part.\n**(2) Records**\nIn carrying out paragraph (1), the Review Board shall consider and render a decision regarding\u2014\n**(A)**\nwhether a record constitutes a missing Armed Forces and civilian personnel record; and\n**(B)**\nwhether a missing Armed Forces and civilian personnel record, or particular information in a missing Armed Forces and civilian personnel record, qualifies for postponement of disclosure under this Act.\n##### (j) Powers\n**(1) In general**\nThe Review Board shall have the authority to act in a manner prescribed under this Act, including the authority to\u2014\n**(A)**\ndirect Government offices to transmit to the Archivist missing Armed Forces and civilian personnel records as required under this Act;\n**(B)**\ndirect Government offices to transmit to the Archivist substitutes and summaries of missing Armed Forces and civilian personnel records that can be publicly disclosed to the fullest extent for any missing Armed Forces and civilian personnel record that is proposed for postponement in full or that is substantially redacted;\n**(C)**\nobtain access to missing Armed Forces and civilian personnel records that have been identified by a Government office;\n**(D)**\ndirect a Government office to make available to the Review Board, and if necessary investigate the facts surrounding, additional information, records, or testimony from individuals, which the Review Board has reason to believe is required to fulfill the functions and responsibilities of the Review Board under this Act;\n**(E)**\nhold such hearings, sit and act at such times and places, take such testimony, receive such evidence, administer such oaths, and subpoena documents as the Review Board considers advisable to carry out the responsibilities of the Review Board under this Act;\n**(F)**\nsubpoena private persons to compel the production of documents and other records relevant to the responsibilities of the Review Board under this Act;\n**(G)**\nrequire any Government office to account in writing for the destruction of any records relating to the loss, fate, or status of missing Armed Forces and civilian personnel;\n**(H)**\nreceive information from the public regarding the identification and public disclosure of missing Armed Forces and civilian personnel records; and\n**(I)**\nmake a final determination regarding whether a missing Armed Forces and civilian personnel record will be disclosed to the public or disclosure of the missing Armed Forces and civilian personnel record to the public will be postponed, notwithstanding the determination of an Executive agency.\n**(2) Enforcement of subpoenas**\nAny subpoena issued under the Review Board under this subsection may be enforced by any appropriate Federal court acting pursuant to a lawful request of the Review Board.\n##### (k) Presidential authority over review board determination\n**(1) Public disclosure or postponement of disclosure**\nAfter the Review Board has made a formal determination concerning the public disclosure or postponement of disclosure of an missing Armed Forces and civilian personnel record or information contained in a missing Armed Forces and civilian personnel record, obtained or developed solely within the executive branch, the President\u2014\n**(A)**\nshall have the sole and nondelegable authority to require the disclosure or postponement of such record or information under the standards set forth in sections 5 and 6; and\n**(B)**\nshall provide the Review Board with an unclassified written certification specifying the President\u2019s decision within 30 days after the Review Board\u2019s determination and notice to the executive agency as required under this Act, stating the justification for the President\u2019s decision, including the applicable grounds for postponement under section 6.\n**(2) Periodic review**\nAny missing Armed Forces and civilian personnel record for which public disclosure is postponed by the President shall be subject to the requirements of periodic review and declassification of classified information and public disclosure in the Collection set forth in section 5.\n**(3) Record of presidential postponement**\nThe Review Board shall, upon its receipt, publish in the Federal Register a copy of any unclassified written certification, statement, or other materials transmitted by or on behalf of the President with regard to postponement of the public disclosure of missing Armed Forces and civilian personnel records under section 6.\n##### (l) Witness immunity\nThe Review Board shall be considered to be an agency of the United States for purposes of section 6001 of title 18, United States Code.\n##### (m) Oversight\n**(1) In general**\nThe Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives shall\u2014\n**(A)**\nhave continuing legislative oversight jurisdiction with respect to the official conduct of the Review Board and the disposition of postponed records after termination of the Review Board; and\n**(B)**\nnot later than 10 days after submitting a request, be provided access to any records held or created by the Review Board.\n**(2) Duty of Review Board**\nThe Review Board shall have the duty to cooperate with the exercise of oversight jurisdiction under paragraph (1).\n**(3) Security clearances**\nThe Chair and Ranking Members of the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives, and designated Committee staff, shall be granted all security clearances and accesses held by the Review Board, including to relevant Presidential and department or agency special access and compartmented access programs.\n##### (n) Support services\nThe Administrator of General Services shall provide administrative services for the Review Board on a reimbursable basis.\n##### (o) Interpretive regulations\nThe Review Board may issue interpretive regulations if the Review Board finds such regulation to be necessary and appropriate.\n##### (p) Termination and Winding Up\n**(1) In general**\nOn the date that is 2 years after the date of enactment of this Act, the Review Board shall, by majority vote, determine whether all Government offices have complied with the obligations, mandates, and directives under this Act.\n**(2) Termination date**\nThe Review Board shall terminate on the date that is 4 years after the date on which members of the Review Board are sworn in to the Review Board.\n**(3) Report**\nBefore the termination of the Review Board under paragraph (2), the Review Board shall submit to Congress reports, including a complete and accurate accounting of expenditures during its existence, and shall complete all other reporting requirements under this Act.\n**(4) Records**\nUpon termination of the Review Board, the Review Board shall transfer all records of the Review Board to the Archivist for inclusion in the Collection, and no record of the Review Board shall be destroyed.\n#### 8. Missing Armed Forces and Civilian Personnel Records Review Board personnel\n##### (a) Executive Director\n**(1) In general**\nNot later than 45 days after the initial meeting of the Review Board, the Review Board shall appoint an individual to the position of Executive Director.\n**(2) Qualifications**\nThe individual appointed as Executive Director\u2014\n**(A)**\nshall be a citizen of the United States of integrity and impartiality;\n**(B)**\nshall be appointed without regard to political affiliation; and\n**(C)**\nshall not have any conflict of interest with the mission of the Review Board.\n**(3) Consultation with the Office of Government Ethics**\nIn their consideration of the person to be appointed to the position of Executive Director, the Review Board shall consult with the Director of the Office of Government Ethics to\u2014\n**(A)**\ndetermine criteria for possible conflicts of interest of the Executive Director, consistent with ethics laws, statutes, and regulations for executive branch employees; and\n**(B)**\nensure that no individual selected for such position of Executive Director possesses a conflict of interest as so determined.\n**(4) Security clearance**\n**(A) In general**\nThe individual appointed as Executive Director shall have the security clearance necessary to carry out the duties of the position at the time of appointment.\n**(B) Expedited provision**\nThe appropriate departments, agencies, and elements of the executive branch of the Federal Government shall cooperate to ensure that an application by an individual nominated to be Executive Director, seeking security clearances necessary to carry out the duties of the Executive Director, is expeditiously reviewed and granted or denied.\n**(5) Duties**\nThe Executive Director shall\u2014\n**(A)**\nserve as principal liaison to Government offices;\n**(B)**\nbe responsible for the administration and coordination of the review of records by the Review Board;\n**(C)**\nbe responsible for the administration of all official activities conducted by the Review Board; and\n**(D)**\nnot have the authority to decide or determine whether any record should be disclosed to the public or postponed for disclosure.\n**(6) Removal**\nThe Executive Director may be removed by a majority vote of the Review Board.\n##### (b) Staff\n**(1) In general**\nThe Review Board may, in accordance with the civil service laws, but without regard to civil service law and regulation for competitive service as defined in subchapter I of chapter 33 of title 5, United States Code, appoint and terminate additional employees as are necessary to enable the Review Board and the Executive Director to perform their duties under this Act.\n**(2) Treatment as employees of executive branch**\nThe Executive Director and other employees of the Review Board shall be treated as employees of the executive branch.\n**(3) Qualifications**\nAn individual appointed to a position as an employee of the Review Board\u2014\n**(A)**\nshall be a citizen of the United States of integrity and impartiality; and\n**(B)**\nshall not have had any previous involvement with any official investigation or inquiry relating to the loss, fate, or status of missing Armed Forces and civilian personnel.\n**(4) Consultation with the Office of Government Ethics**\nIn their consideration of persons to be appointed as staff of the Review Board, the Review Board shall consult with the Director of the Office of Government Ethics to\u2014\n**(A)**\ndetermine criteria for possible conflicts of interest of staff of the Review Board, consistent with ethics laws, statutes, and regulations for executive branch employees; and\n**(B)**\nensure that no individual selected for such position of staff of the Review Board possesses a conflict of interest as so determined.\n**(5) Security clearance**\n**(A) In general**\nAn individual appointed as an employee of the Review Board shall have the security clearance necessary to carry out the duties of the position at the time of appointment.\n**(B) Expedited provision**\nThe appropriate departments, agencies, and elements of the executive branch of the Federal Government shall cooperate to ensure that an application by an individual who is a candidate for a position with the Review Board, seeking security clearances necessary to carry out the duties of the position, is expeditiously reviewed and granted or denied.\n##### (c) Compensation\nThe Review Board shall fix the compensation of the Executive Director and other employees of the Review Board described in subsection (b) without regard to chapter 51 and subchapter III of chapter 53 of title 5, United States Code, relating to classification of positions and General Schedule pay rates, except that the rate of pay for the Executive Director and other employees may not exceed the rate payable for level V of the Executive Schedule under section 5316 of title 5, United States Code.\n##### (d) Advisory committees\n**(1) In general**\nThe Review Board may create 1 or more advisory committees to assist in fulfilling the responsibilities of the Review Board under this Act.\n**(2) Applicability of FACA**\nAny advisory committee created by the Review Board shall be subject to chapter 10 of title 5, United States Code.\n#### 9. Review of records by the Missing Armed Forces and Civilian Personnel Records Review Board\n##### (a) Startup requirements\nThe Review Board shall\u2014\n**(1)**\nnot later than 90 days after the date on which all members are sworn in, publish an initial schedule for review of all missing Armed Forces and civilian personnel records, which the Archivist shall highlight and make available on a publicly accessible website administered by the National Archives; and\n**(2)**\nnot later than 180 days after the swearing in of the Review Board members, begin reviewing missing Armed Forces and civilian personnel records, as necessary, under this Act.\n##### (b) Determination of the Review Board\n**(1) In general**\nThe Review Board shall direct that all records that relate, directly or indirectly, to the loss, fate, or status of missing Armed Forces and civilian personnel be transmitted to the Archivist and disclosed to the public in the Collection in the absence of clear and convincing evidence that the record is not a missing Armed Forces and civilian personnel record.\n**(2) Postponement**\nIn approving postponement of public disclosure of a missing Armed Forces and civilian personnel record, or information within a missing Armed Forces and civilian personnel record, the Review Board shall seek to carry out the following:\n**(A)**\nProvide for the disclosure of segregable parts, substitutes, or summaries of the missing Armed Forces and civilian personnel record.\n**(B)**\nDetermine, in consultation with the originating body and consistent with the standards for postponement under this Act, which of the following alternative forms of disclosure shall be made by the originating body:\n**(i)**\nAny reasonably segregable particular information in a missing Armed Forces and civilian personnel record.\n**(ii)**\nA substitute record for that information which is postponed.\n**(iii)**\nA summary of a missing Armed Forces and civilian personnel record.\n**(3) Reporting**\nWith respect to a missing Armed Forces and civilian personnel record, or information within a missing Armed Forces and civilian personnel record, the public disclosure of which is postponed under this Act, or for which only substitutions or summaries have been disclosed to the public, the Review Board shall create and transmit to the Archivist, the Committee on Homeland Security and Governmental Affairs of the Senate, and the Committee on Oversight and Government Reform of the House of Representatives an unclassified and publicly releasable report containing\u2014\n**(A)**\na description of actions by the Review Board, the originating body, or any Government office (including a justification of any such action to postpone disclosure of any record or part of any record) and of any official proceedings conducted by the Review Board; and\n**(B)**\na statement, based on a review of the proceedings and in conformity with the decisions reflected therein, designating a recommended specified time at which, or a specified occurrence following which, the material may be appropriately disclosed to the public under this Act, which the Review Board shall disclose to the public with notice thereof, reasonably calculated to make interested members of the public aware of the existence of the statement.\n**(4) Actions after determination**\n**(A) In general**\nNot later than 30 days after the date of a determination by the Review Board that a missing Armed Forces and civilian personnel record shall be publicly disclosed in the Collection or postponed for disclosure, the Review Board shall notify the head of the originating body of the determination and highlight and make available the determination on a publicly accessible website reasonably calculated to make interested members of the public aware of the existence of the determination.\n**(B) Oversight notice**\nSimultaneous with notice under subparagraph (A), the Review Board shall provide notice of a determination concerning the public disclosure or postponement of disclosure of a missing Armed Forces and civilian personnel record, or information contained within a missing Armed Forces and civilian personnel record, which shall include a written unclassified justification for public disclosure or postponement of disclosure, including an explanation of the application of any standards in section 6 to the President, to the Committee on Homeland Security and Governmental Affairs of the Senate, and the Committee on Oversight and Government Reform of the House of Representatives.\n**(5) Referral after termination**\nA missing Armed Forces and civilian personnel record that is identified, located, or otherwise discovered after the date on which the Review Board terminates shall be transmitted to the Archivist for the Collection and referred to the Committee on Armed Services of the Senate and the Committee on Armed Services of the House of Representatives for review, ongoing oversight and, as warranted, referral for possible enforcement action relating to a violation of this Act and determination as to whether declassification of the missing Armed Forces and civilian personnel is warranted under this Act.\n##### (c) Notice to public\nEvery 30 days, beginning on the date that is 60 days after the date on which the Review Board first approves the postponement of disclosure of a missing Armed Forces and civilian personnel record, the Review Board shall highlight and make accessible on a publicly available website reasonably calculated to make interested members of the public aware of the existence of the postponement a notice that summarizes the postponements approved by the Review Board, including a description of the subject, originating body, length or other physical description, and each ground for postponement that is relied upon.\n##### (d) Reports by the Review Board\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, and every year thereafter until the Review Board terminates, the Review Board shall submit a report regarding the activities of the Review Board to\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(B)**\nthe Committee on Oversight and Government Reform of the House of Representatives;\n**(C)**\nthe President;\n**(D)**\nthe Archivist; and\n**(E)**\nthe head of any Government office the records of which have been the subject of Review Board activity.\n**(2) Contents**\nEach report under paragraph (1) shall include the following information:\n**(A)**\nA financial report of the expenses for all official activities and requirements of the Review Board and its employees.\n**(B)**\nThe progress made on review, transmission to the Archivist, and public disclosure of missing Armed Forces and civilian personnel records.\n**(C)**\nThe estimated time and volume of missing Armed Forces and civilian personnel records involved in the completion of the duties of the Review Board under this Act.\n**(D)**\nAny special problems, including requests and the level of cooperation of Government offices, with regard to the ability of the Review Board to carry out its duties under this Act.\n**(E)**\nA record of review activities, including a record of postponement decisions by the Review Board or other related actions authorized under this Act, and a record of the volume of records reviewed and postponed.\n**(F)**\nSuggestions and requests to Congress for additional legislative authority needs.\n**(G)**\nAn appendix containing copies of reports relating to postponed records submitted to the Archivist under subsection (b)(3) since the end of the period covered by the most recent report under paragraph (1).\n**(3) Copies and briefs**\nCoincident with the reporting requirements in paragraph (2), or more frequently as warranted by new information, the Review Board shall provide copies to, and fully brief, at a minimum, the President, the Archivist, leadership of Congress, the Chair and Ranking Members of the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives, and the Chairs, Ranking Members, Vice Chairs, as the case may be, of such other committees as leadership of Congress determines appropriate on\u2014\n**(A)**\nrecommendations for periodic review, downgrading, and declassification, as well as the exact time or specified occurrence following which specific missing Armed Forces and civilian material may be appropriately disclosed;\n**(B)**\nthe rationale behind each postponement determination and the recommended means to achieve disclosure of each postponed item;\n**(C)**\nany other findings that the Review Board chooses to offer; and\n**(D)**\nan addendum containing copies of reports of postponed records to the Archivist required under subsection (b)(3) made since the date of the preceding report under this subsection.\n**(4) Termination notice**\nNot later than 90 days before the Review Board expects to complete the work of the Review Board under this Act, the Review Board shall provide written notice to Congress of the intent of the Review Board to terminate operations at a specified date.\n#### 10. Disclosure of other materials and additional study\n##### (a) Materials under seal of court\n**(1) In general**\nThe Review Board may request the Attorney General to petition any court of the United States or of a foreign country to release any information relevant to the loss, fate, or status of missing Armed Forces and civilian personnel that is held under seal of the court.\n**(2) Grand jury information**\n**(A) In general**\nThe Review Board may request the Attorney General to petition any court of the United States to release any information relevant to loss, fate, or status of missing Armed Forces and civilian personnel that is held under the injunction of secrecy of a grand jury.\n**(B) Treatment**\nA request for disclosure of missing Armed Forces and civilian personnel materials under this Act shall be deemed to constitute a showing of particularized need under rule 6 of the Federal Rules of Criminal Procedure.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Attorney General should assist the Review Board in good faith to unseal any records that the Review Board determines to be relevant and held under seal by a court or under the injunction of secrecy of a grand jury;\n**(2)**\nthe Secretary of State should\u2014\n**(A)**\ncontact the Governments of the Russian Federation, the People\u2019s Republic of China, and the Democratic People\u2019s Republic of Korea to seek the disclosure of all records in their respective custody, possession, or control relevant to the loss, fate, or status of missing Armed Forces and civilian personnel; and\n**(B)**\ncontact any other foreign government that may hold information relevant to the loss, fate, or status of missing Armed Forces and civilian personnel, and seek disclosure of such information; and\n**(3)**\nall agencies should cooperate in full with the Review Board to seek the disclosure of all information relevant to the loss, fate, or status of missing Armed Forces and civilian personnel consistent with the public interest.\n#### 11. Rules of construction\n##### (a) Precedence over other law\nWhen this Act requires transmission of a record to the Archivist or public disclosure, it shall take precedence over any other law (except section 6103 of the Internal Revenue Code of 1986), judicial decision construing such law, or common law doctrine that would otherwise prohibit such transmission or disclosure, with the exception of deeds governing access to or transfer or release of gifts and donations of records to the United States Government.\n##### (b) Freedom of Information Act\nNothing in this Act shall be construed to eliminate or limit any right to file requests with any Executive agency or seek judicial review of the decisions under section 552 of title 5, United States Code.\n##### (c) Judicial review\nNothing in this Act shall be construed to preclude judicial review under chapter 7 of title 5, United States Code, of final actions taken or required to be taken under this Act.\n##### (d) Existing authority\nNothing in this Act revokes or limits the existing authority of the President, any Executive agency, the Senate, or the House of Representatives, or any other entity of the Government to publicly disclose records in its custody, possession, or control.\n##### (e) Rules of the Senate and House of Representatives\nTo the extent that any provision of this Act establishes a procedure to be followed in the Senate or the House of Representatives, such provision is adopted\u2014\n**(1)**\nas an exercise of the rulemaking power of the Senate and House of Representatives, respectively, and is deemed to be part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House, and it supersedes other rules only to the extent that it is inconsistent with such rules; and\n**(2)**\nwith full recognition of the constitutional right of either House to change the rules (so far as they relate to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.\n#### 12. Requests for extensions\n##### (a) In general\nThe head of a Government office required to comply with a deadline under this Act that is based on the date of establishment of a quorum of the members of the Review Board under section 7 may request an extension from the Review Board for good cause.\n##### (b) Extended deadline\nIf the Review Board agrees to the request, the deadline applicable to the Government office for the purpose of such requirement shall be such later date as the Review Board may determine appropriate.\n#### 13. Termination of effect of Act\n##### (a) Provisions pertaining to the Review Board\nThe provisions of this Act that pertain to the appointment and operation of the Review Board shall cease to be effective when the Review Board and the terms of its members have terminated under section 7(p).\n##### (b) Other provisions\nThe remaining provisions of this Act shall continue in effect until such time as the Archivist certifies to the President and Congress that all missing Armed Forces and civilian personnel records have been made available to the public in accordance with this Act.\n#### 14. Authorization of appropriations\nThere are authorized to be appropriated such sums as are necessary to carry out this Act, to remain available until expended.\n#### 15. Severability\nIf any provision of this Act, or the application thereof to any person or circumstance, is held invalid, the remainder of this Act and the application of that provision to other persons not similarly situated or to other circumstances shall not be affected by the invalidation.",
      "versionDate": "2025-11-19",
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
        "actionDate": "2025-12-15",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "6723",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Bring Our Heroes Home Act",
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
        "updateDate": "2026-01-08T16:25:28Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3226is.xml"
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
      "title": "Bring Our Heroes Home Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Bring Our Heroes Home Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the creation of the missing Armed Forces and civilian personnel Records Collection at the National Archives, to require the expeditious public transmission to the Archivist and public disclosure of missing Armed Forces and civilian personnel records, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T05:48:19Z"
    }
  ]
}
```
